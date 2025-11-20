def game_loop(handler):
    
    if not handler.quiz_game_data:
        handler._load_quiz_game_data()
    
    questions = handler.quiz_game_data
    
    if not questions:
        print("No questions available for this game.")
        handler.navigate_to("main")
        return
    
    print("Let's test your knowledge!")
    
    handler.user_answers = []
    
    for question_num, question_data in enumerate(questions, 1):
        print(f"\nQuestion {question_num}/{len(questions)}: {question_data['question']}")
        
        options = question_data['options']
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                user_input = input("\nChoose an answer (1-{}) or Q to quit: ".format(len(options))).strip()
                
                if user_input.lower() == 'q':
                    print("Quitting quiz...")
                    handler.navigate_to("main")
                    return
                
                selected_index = int(user_input) - 1 
                
                if 0 <= selected_index < len(options):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except (EOFError, KeyboardInterrupt):
                print("\nQuitting quiz...")
                handler.navigate_to("main")
                return
        
        handler.user_answers.append({
            'questionID': question_data['questionID'],
            'question': question_data['question'],
            'selected_index': selected_index,
            'selected_answer': options[selected_index],
            'correct_index': question_data['correct_answer'],
            'correct_answer': options[question_data['correct_answer']],
            'is_correct': selected_index == question_data['correct_answer'],
            'options': options,
            'game_name': question_data.get('game_name', 'Unknown')
        })
        
        if selected_index == question_data['correct_answer']:
            print("✓ Correct!")
        else:
            print(f"✗ Wrong! The correct answer was: {options[question_data['correct_answer']]}")
    
    correct_count = sum(1 for answer in handler.user_answers if answer['is_correct'])
    total_questions = len(handler.user_answers)
    percentage = (correct_count / total_questions * 100) if total_questions > 0 else 0
    
    handler.results_data = {
        'correct': correct_count,
        'total': total_questions,
        'percentage': percentage,
        'answers': handler.user_answers
    }
    
    handler.navigate_to("results")

import string

def game_loop(handler):
    term = handler.term

    handler._load_quiz_game_data()
    question = handler.quiz_game_data

    handler.user_answers = []
    handler.results_data = []
    handler.review_data = []

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        for question_number, question in enumerate(question, start=1):
            handler.review_data.append(question['correct_answer'])
            options = question['options']
            selected_index = 0
            while True:
                print(term.clear)
                print(term.center(f"Question {question_number}: {question['question']}" + term.normal))
                print()

                for i, option in enumerate(options):
                    label = string.ascii_uppercase[i]
                    max_label_len = max(len(f"{string.ascii_uppercase[j]}. ") for j in range(len(options)))
                    max_option_len = max(len(opt) for opt in options)
                    text_label = f"{label}. ".ljust(max_label_len)
                    text_option = option.center(max_option_len)
                    line = f"{text_label}{text_option}"
                    if i == selected_index:
                        print(term.center(term.black_on_white + f"➤ {line}" + term.normal))
                    else:
                        print(term.center(f"  {line}" + term.normal))
                
                print()
                print(term.center(term.bold + term.cyan + "↑/↓ Navigate | Enter to select" + term.normal))

                key = term.inkey()
                if key.code == term.KEY_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif key.code == term.KEY_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif key.code == term.KEY_LEFT or key.code == term.KEY_RIGHT:
                    continue
                elif key.code == term.KEY_ENTER:
                    handler.user_answers.append(selected_index)
                    is_correct = selected_index == question['correct_answer']
                    handler.results_data.append("right" if is_correct else "wrong")
                    break
                else:
                    key_str = str(key).lower()
                    if key_str and len(key_str) == 1 and 'a' <= key_str <= 'd':
                        letter_index = ord(key_str) - ord('a')
                        if letter_index < len(options):
                            handler.user_answers.append(letter_index)
                            is_correct = letter_index == question['correct_answer']
                            handler.results_data.append("right" if is_correct else "wrong")
                            break
        handler.navigate_to('results')


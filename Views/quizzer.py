
def game_loop(handler):

    if not handler.quiz_game_data:
        handler._load_quiz_game_data()

    question = handler.quiz_game_data
    for question_num, question_data in enumerate(question, 1):
        print(question_num)
        print(question_data)

    print("Let's test your knowledge!")
    answers = handler.user_answers
    right_wrong = handler.results_data
    correct = handler.review_data
    question_number = 0

    for i in question:
        correct.append(i['correct_answer'])
        print(correct)
        print(f"Question {question_number+1}: {i['question']}")
        for j, k in enumerate(i['options'], 1):
            print(f"{j}. {k}")

        question_number += 1

        selected_index = int(input("Choose an answer: "))-1
        answers.append(selected_index)
        print(answers)

        if selected_index == i['correct_answer']:
            right_wrong.append("right")
            print(right_wrong)
        else:
            right_wrong.append("wrong")
            print(right_wrong)
        handler.navigate_to('results')

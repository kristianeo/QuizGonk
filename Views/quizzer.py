
def game_loop(handler):

    if not handler.quiz_game_data:
        handler._load_quiz_game_data()

    question = handler.quiz_game_data

    handler.user_answers = []
    handler.results_data = []
    handler.review_data = []

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

        handler.navigate_to('results')

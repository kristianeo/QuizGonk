import os

def game_loop(handler):

    if not handler.quiz_game_data:
        handler._load_quiz_game_data()

    question = handler.quiz_game_data

    handler.user_answers = []
    handler.results_data = []
    handler.review_data = []

    print("Let's test your knowledge!")
    user_answers = handler.user_answers
    right_wrong = handler.results_data
    correct_index = handler.review_data
    question_number = 0

    for i in question:
        os.system('cls' if os.name == 'nt' else 'clear')
        correct_index.append(i['correct_answer'])
        print(correct_index)
        print(f"Question {question_number+1}: {i['question']}")
        for j, k in enumerate(i['options'], 1):
            print(f"{j}. {k}")
        question_number += 1
        while True:
            try:
                selected_index = int(input("Choose an answer: "))-1
                if 0 <= selected_index < 4:
                    user_answers.append(selected_index)
                    if selected_index == i['correct_answer']:
                        right_wrong.append("right")
                    else:
                        right_wrong.append("wrong")
                    break
                else:
                    print("Please enter a number from 1-4...")
            except ValueError:
                print("Please enter a number from 1-4...")

    handler.navigate_to('results')
    os.system('cls' if os.name == 'nt' else 'clear')

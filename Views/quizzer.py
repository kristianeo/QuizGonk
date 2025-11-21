import os
import string

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
        print(f"Question {question_number+1}: {i['question']}")
        for o, option in zip(string.ascii_uppercase, i['options']):
            print(f'{o}. {option}')
        question_number += 1

        while True:
            try:
                selected_answer = str(input("Choose an answer: ")).lower().strip()
                if selected_answer == 'a':
                    selected_index = 0
                    user_answers.append(selected_index)
                    if selected_index == i['correct_answer']:
                        right_wrong.append("right")
                    else:
                        right_wrong.append("wrong")
                    break
                elif selected_answer == 'b':
                    selected_index = 1
                    user_answers.append(selected_index)
                    if selected_index == i['correct_answer']:
                        right_wrong.append("right")
                    else:
                        right_wrong.append("wrong")
                    break
                elif selected_answer == 'c':
                    selected_index = 2
                    user_answers.append(selected_index)
                    if selected_index == i['correct_answer']:
                        right_wrong.append("right")
                    else:
                        right_wrong.append("wrong")
                    break
                elif selected_answer == 'd':
                    selected_index = 3
                    user_answers.append(selected_index)
                    if selected_index == i['correct_answer']:
                        right_wrong.append("right")
                    else:
                        right_wrong.append("wrong")
                    break
                else:
                    print("Please enter option A, B, C or D...")
            except ValueError:
                print("Please enter option A, B, C or D...")

    handler.navigate_to('results')
    os.system('cls' if os.name == 'nt' else 'clear')

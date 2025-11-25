import os
import string
from tkinter import *

def game_loop(handler, root):

    frame = Frame(root)
    handler._load_quiz_game_data()

    question = handler.quiz_game_data

    handler.user_answers = []
    handler.results_data = []
    handler.review_data = []

    label_start = Label(root, text="Let's test your knowledge!")
    label_start.pack()

    user_answers = handler.user_answers
    right_wrong = handler.results_data
    correct_index = handler.review_data
    question_number = 0

    for i in question:
        os.system('cls' if os.name == 'nt' else 'clear')
        correct_index.append(i['correct_answer'])
        question_label = Label(frame, text=f"Question {question_number+1}: {i['question']}")
        question_label.pack()
        for o, option in zip(string.ascii_uppercase, i['options']):
            options_button = Button(frame, text=f'{o}. {option}', command=lambda: push_button(handler, o))
            options_button.pack()
        question_number += 1

def push_button(handler, o):
    selected_answer = o
    if selected_answer == 'A':
        selected_index = 0
        handler.user_answers.append(selected_index)
    if selected_answer == 'B':
        selected_index = 1
        handler.user_answers.append(selected_index)
    if selected_answer == 'C':
        selected_index = 2
        handler.user_answers.append(selected_index)
    if selected_answer == 'D':
        selected_index = 3
        handler.user_answers.append(selected_index)

    return Frame

import string

def show_review(handler):
    term = handler.term
    print()

    user_answers = handler.user_answers
    right_wrong = handler.results_data
    questions = handler.quiz_game_data

    keep = [i for i, val in enumerate(right_wrong) if val == "wrong"]
    user_answers = [user_answers[i] for i in keep]
    questions = [questions[i] for i in keep]

    current = 0
    with (term.fullscreen(), term.cbreak(), term.hidden_cursor()):
        if not questions:
            print(term.center("No wrong answers to review."))
            handler.navigate_to('main')
            return
        total_wrong = len(questions)
        while True:
            while 0 <= current < total_wrong:
                print(term.clear)
                print(term.center(term.bold + f"You got {total_wrong} questions wrong!") + term.normal)
                print()
                question = questions[current]
                print(term.center(f'Question {current + 1} of {total_wrong}:'))
                print(term.center(f"{question.get('question', '<no question>')}"))
                print()

                correct_index = question.get('correct_answer')
                user_index = None
                if 0 <= current < len(user_answers):
                    user_index = user_answers[current]

                for letter, (index, option) in zip(string.ascii_uppercase, enumerate(question.get('options', []))):
                    if index == correct_index:
                        colored_option = term.green + f"{letter}. {option}" + term.normal
                    elif index == user_index:
                        colored_option = term.red + f"{letter}. {option}" + term.normal
                    else:
                        colored_option = f'{letter}. {option}'
                    line = colored_option
                    print(term.center(line))

                print()
                print(term.center(term.bold + term.cyan + "→/← to Navigate | M for main menu | Q or X to quit" + term.normal))

                key = term.inkey()

                if key.code == term.KEY_LEFT:
                    current = (current -1) % len(questions)
                elif key.code == term.KEY_RIGHT:
                    current = (current + 1) % len(questions)
                elif key.lower() in ('q', 'x'):
                    handler.quit()
                    return
                elif key.lower() == 'm':
                    handler.navigate_to("menu")
                    return


import os
def show_review(handler):
    print("Review")

    user_answers = handler.user_answers
    right_wrong = handler.results_data
    questions = handler.quiz_game_data

    keep = [i for i, val in enumerate(right_wrong) if val == "wrong"]
    user_answers = [user_answers[i] for i in keep]
    right_wrong = [right_wrong[i] for i in keep]
    questions = [questions[i] for i in keep]

    if not questions:
        print("No wrong answers to review.")
        handler.navigate_to('main')
        return

    current = 0
    while True:
        total_wrong = len(questions)
        print("You got", total_wrong, "questions wrong!")
        print("Let's review them")

        while 0 <= current < total_wrong:
            os.system('cls' if os.name == 'nt' else 'clear')
            question = questions[current]
            print("\nQuestion {}: {}".format(current + 1, question.get('question', '<no question>')))

            correct_index = question.get('correct_answer')
            user_index = None
            if 0 <= current < len(user_answers):
                user_index = user_answers[current]

            for index, option in enumerate(question.get('options', [])):
                markers = []
                if correct_index is not None and index == correct_index:
                    markers.append("<--- Correct")
                if user_index is not None and index == user_index:
                    markers.append("<--- You answered")
                marker_text = " | ".join(markers)
                print("  {}. {} {}".format(index + 1, option, marker_text))

            user_input = input("Enter 'n' for next, 'p' for previous, 'm' to return to main menu: ").strip().lower()

            if user_input == "n":
                if current < total_wrong - 1:
                    current += 1
                else:
                    print("Already at last question.")
            elif user_input =="p":
                if current > 0:
                    current -= 1
                else:
                    print("Already at first question.")
            elif user_input == "m":
                handler.navigate_to('main')
                os.system('cls' if os.name == 'nt' else 'clear')
                return

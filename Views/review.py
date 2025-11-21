def show_review(handler):
    print("Review")

    user_answers = handler.user_answers
    right_wrong = handler.results_data
    correct_index = handler.review_data
    questions = handler.quiz_game_data

    print(questions)

    indices_to_remove = [i for i, val in enumerate(right_wrong) if val == "right"]
    for i in reversed(indices_to_remove):
        user_answers.pop(i)
        correct_index.pop(i)
        questions.pop(i)
        right_wrong.pop(i)
        
    current = 0
    while True:
        print("You got ", len(right_wrong), " questions wrong!")
        print("Let's review them")

        while 0 <= current < len(questions):
            print("\nQuestion {}: {}".format(current + 1, questions[current]['question']))
            for index, options in enumerate(questions[current]['answers']):
                marker = ""
                if index == correct_index[current]:
                    marker += "<--- Correct"
                if index == user_answers[current]:
                    if marker:
                        marker += " | "
                    marker += "<--- You answered"
                print("  {}. {} {}".format(index + 1, answer, marker))
            user_input = input("Enter 'n' for next, '+' for previous, 'x' or 'q' to exit review: ").strip().lower()
            if user_input == "n":
                current += 1
            elif user_input == "+":
                current -= 1
            elif user_input in ("x", "q"):
                handler.navigate_to('main')
                return

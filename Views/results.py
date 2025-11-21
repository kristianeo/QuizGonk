import os

def show_results(handler):
    results_data_check = handler.results_data

    right_count = 0
    wrong_count = 0

    for results in results_data_check:
        if results == "wrong":
            wrong_count += 1
        else:
            right_count += 1

    accuracy = (right_count/(right_count + wrong_count))*100
    formatted_accuracy = f"{accuracy:.2f}"

    print(f"\nResults Summary:\n\nRight answers: {right_count}\nWrong answers: "
          f"{wrong_count}\nAccuracy: {formatted_accuracy}%\n")

    if wrong_count == 0:
        print("Congratulations! You dont need a review.\n")
        user_input = input("Press enter to return to main menu. Q or X to quit.")
        ui = user_input.lower().strip()
        if ui in ("q", "x"):
            print("Goodbye.")
            handler.quit()
            return
        else:
            handler.navigate_to("main")
            os.system('cls' if os.name == 'nt' else 'clear')
            return

    wait_for_user = True
    while wait_for_user:
        try:
            user_input = input("Do you want a review? (y/n): ").strip().lower()
            if user_input == 'y':
                handler.navigate_to("review")
                os.system('cls' if os.name == 'nt' else 'clear')
                wait_for_user = False
            elif user_input == 'n':
                handler.navigate_to("main")
                os.system('cls' if os.name == 'nt' else 'clear')
                wait_for_user = False
            else:
                print("Invalid input. Please select yes for review, or chose no to go back to main menu.")
        except ValueError:
            print("Invalid input. Please select yes for review, or chose no to go to main menu.")
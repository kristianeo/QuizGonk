def show_results(handler):
    print("Results Summary")

    wait_for_user = True
    while wait_for_user:
        user_input = input("Type 'end' to finish the game: ").strip().lower()
        if user_input == 'end':
            wait_for_user = False
    handler.navigate_to("review")
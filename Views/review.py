def show_review(handler):
    print("Review")

    wait_for_user = True
    while wait_for_user:
        user_input = input("Type 'end' to finish the review: ").strip().lower()
        if user_input == 'end':
            wait_for_user = False
    handler.navigate_to("main")
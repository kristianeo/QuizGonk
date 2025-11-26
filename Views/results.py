def show_results(handler):
    term = handler.term
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

    def ascii_printer(score):
        try:
            s = float(score)
        except (TypeError, ValueError):
            try:
                s = float(str(score).strip().strip('%'))
            except Exception:
                s = 0.0

        ascii_flawless = [
            " _____ _                _               _ ",
            "|  ___| | __ ___      _| | ___  ___ ___| |",
            "| |_  | |/ _` \\ \\ /\\ / / |/ _ \\/ __/ __| |",
            "|  _| | | (_| |\\ V  V /| |  __/\\__ \\__ \\_|",
            "|_|   |_|\\__,_| \\_/\\_/ |_|\\___||___/___(_)"
        ]

        ascii_excellent = [
            " _____              _ _            _   _ ",
            "| ____|_  _____ ___| | | ___ _ __ | |_| |",
            "|  _| \\ \\/ / __/ _ \\ | |/ _ \\ '_ \\| __| |",
            "| |___ >  < (_|  __/ | |  __/ | | | |_|_|",
            "|_____/_/\\_\\___\\___|_|_|\\___|_| |_|\\__(_)"
        ]

        ascii_good = [
            "  ____                 _ _ ",
            " / ___| ___   ___   __| | |",
            "| |  _ / _ \\ / _ \\ / _` | |",
            "| |_| | (_) | (_) | (_| |_|",
            " \\____|\\___/ \\___/ \\__,_(_)"
        ]

        ascii_terrible = [
            " _____              _ _     _      _ ",
            "|_   _|__ _ __ _ __(_) |__ | | ___| |",
            "  | |/ _ \\ '__| '__| | '_ \\| |/ _ \\ |",
            "  | |  __/ |  | |  | | |_) | |  __/_|",
            "  |_|\\___|_|  |_|  |_|_.__/|_|\\___(_)"
        ]
        ascii_gonk = [
            "  ____  ___  _   _ _  ___ ",
            " / ___|/ _ \\| \\ | | |/ / |",
            "| |  _| | | |  \\| | ' /| |",
            "| |_| | |_| | |\\  | . \\|_|",
            " \\____|\\___/|_| \\_|_|\\_(_)"
        ]

        if s >= 100:
            art = ascii_flawless
        elif s >= 75:
            art = ascii_excellent
        elif s >= 40:
            art = ascii_good
        elif s >= 10:
            art = ascii_terrible
        else:
            art = ascii_gonk

        for line in art:
            print(term.center(term.bold + term.cyan + line + term.normal))

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.clear)
            ascii_printer(formatted_accuracy)

            print()
            print()
            print(term.center(f"Total questions: {len(results_data_check)}"))  
            print(term.center(f"Right answers: {right_count}"))
            print(term.center(f"Wrong answers: {wrong_count}"))          
            print(term.center(f"Accuracy: {formatted_accuracy}%"))
            print()
            
            if wrong_count == 0:
                print(term.center(term.green + "Congratulations! You got everything right. No review needed." + term.normal))
                print()
                print(term.center(term.cyan + term.bold + "Press any key to return to main menu, or Q/X to quit" + term.normal))
                key = term.inkey()
                if key.lower() in ('q', 'x'):
                    handler.quit()
                    return
                else:
                    handler.navigate_to("main")
                    return
            else:
                print(term.center("Do you want a review? Y for yes, N for no" + term.normal))
                print(term.center(term.cyan + term.bold + "Y/N | Q/X to quit" + term.normal))
                
                key = term.inkey()
                if key.lower() == 'y':
                    handler.navigate_to("review")
                    return
                elif key.lower() == 'n':
                    handler.navigate_to("main")
                    return
                elif key.lower() in ('q', 'x'):
                    handler.quit()
                    return
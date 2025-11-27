import time

def show_credits(handler):
    term = handler.term
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear)

        ascii_art = [
            ".----------------------------------------------.",
            "|    ___        _      ____             _      |",
            "|   / _ \\ _   _(_)____/ ___| ___  _ __ | | __  |",
            "|  | | | | | | | |_  / |  _ / _ \\| '_ \\| |/ /  |",
            "|  | |_| | |_| | |/ /| |_| | (_) | | | |   <   |",
            "|   \\__\\_\\_____|_/___|\\____|\\___/|_| |_|_|\\_\\  |",
            "|                                              |",
            "'----------------------------------------------'"
        ]
        for line in ascii_art:
            print(term.center(term.bold + term.cyan + line + term.normal))

        print()
        print(term.center(term.italic +  'A game made by Thomas Eikhaugen and Kristiane Olsen' + term.normal))

        time.sleep(3)

        print(term.clear)
        print(term.center('*A special thanks to Craig*'))

        time.sleep(3)

        handler.quit()
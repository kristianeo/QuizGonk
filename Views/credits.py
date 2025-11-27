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
        # I tried to make this italic but apparently it's not supported:
        print(term.center('A game made by Thomas Eikhaugen and Kristiane Olsen'))

        time.sleep(5)

        print(term.clear)
        print()
        print()
        print()
        print(term.center('*A special thanks to Craig*'))

        time.sleep(5)

        handler.quit()
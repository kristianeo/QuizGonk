def mainMenu(handler):
    term = handler.term
    
    if not handler.quiz_summary.get('games'):
        handler._load_quiz_summary()
    
    games = handler.quiz_summary.get('games', [])
    handler.quiz_game_data = []
    
    menu_options = []
    for i, game in enumerate(games):
        menu_options.append({
            'label': f"{game['name']} ({game['questions']} questions)",
            'value': str(i + 1)
        })
    
    total = handler.quiz_summary.get('total_questions', 0)
    mixed_count = min(15, total) if total > 0 else 15
    menu_options.append({
        'label': f"Mixed game ({mixed_count} random questions)",
        'value': 'm'
    })
    
    selected_index = 0
    
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)

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
            
            if not games:
                print(term.center(term.yellow("No games available.")))
            else:
                for i, option in enumerate(menu_options):
                    if i == selected_index:
                        print(term.center(term.black_on_white + f"➤ {option['label']}" + term.normal))
                    else:
                        print(term.center(f"  {option['label']}"))
            
            print()
            print(term.center(term.bold + term.cyan + "↑/↓ Navigate | Enter to select | Q to quit" + term.normal))
            
            key = term.inkey()
            
            if key.code == term.KEY_UP:
                selected_index = (selected_index - 1) % len(menu_options)
            elif key.code == term.KEY_DOWN:
                selected_index = (selected_index + 1) % len(menu_options)
            elif key.code == term.KEY_ENTER:
                selected_value = menu_options[selected_index]['value']
                if selected_value == 'm':
                    handler.selected_game = "m"
                    handler.navigate_to("quiz")
                    return
                else:
                    handler.selected_game = selected_value
                    handler.navigate_to("quiz")
                    return
            elif key.lower() in 'q':
                handler.navigate_to('credits')
                return
            elif key.isdigit():
                index = int(key) - 1
                if 0 <= index < len(games):
                    handler.selected_game = key
                    handler.navigate_to("quiz")
                    return
            elif key.lower() == 'm':
                handler.selected_game = "m"
                handler.navigate_to("quiz")
                return

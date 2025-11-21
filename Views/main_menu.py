import os
def mainMenu(handler):
    # Load quiz summary if not already loaded
    if not handler.quiz_summary.get('games'):
        handler._load_quiz_summary()
    
    games = handler.quiz_summary.get('games', [])
    
    while True:
        try:
            print("""
            ╔════════════╗
            ║  QuizGonk  ║
            ╚════════════╝
            """)
            if not games:
                print("No games available.")
            else:
                for i, game in enumerate(games):
                    game_name = game.get('name', f'Game {i+1}')
                    print(f"{i+1}. {game_name} ({game['questions']} questions)")
                total = handler.quiz_summary.get('total_questions', 0)
                mixed_count = min(15, total) if total > 0 else 15
                print(f"M. Mixed game ({mixed_count} random questions)")
            print("Q or X. Quit")
            userInput = input("Select option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            handler.quit()
            return

        if not userInput:
            continue

        ui = userInput.lower()
        if ui in ("q", "x"):
            print("Goodbye.")
            handler.quit()
            return

        if ui == "m":
            handler.selected_game = "m"
            handler.navigate_to("quiz")
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        if userInput.isdigit():
            index = int(userInput) - 1
            if 0 <= index < len(games):
                handler.selected_game = userInput
                handler.navigate_to("quiz")
                os.system('cls' if os.name == 'nt' else 'clear')
                
                return
            else:
                print(f"Please select a number between 1 and {len(games)}.")
                continue

        print("Invalid input. Please enter a number, 'm' for mixed game, or 'q' to quit.")

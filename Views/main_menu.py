
from pathlib import Path
from Views.quizzer import gameLoop

def mainMenu(data):
    games = data
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
                    print(f"{i+1}. {game.get('name', 'Game')} ({len(game.get('questions', []))} questions)")
                print("M. Mixed game (All questions)")
            print("Q or X. Quit")
            userInput = input("Select option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return None

        if not userInput:
            continue

        ui = userInput.lower()
        if ui in ("q", "x"):
            print("Goodbye.")
            return None

        if ui == "m":
            mixed_questions = []
            for g in games:
                mixed_questions.extend(g.get("questions", []))
            mixed_game = {"questions": mixed_questions}
            gameLoop(mixed_game)
            return None

        if userInput.isdigit():
            idx = int(userInput) - 1
            if 0 <= idx < len(games):
                gameLoop(games[idx])
                return None
            else:
                print(f"Please select a number between 1 and {len(games)}.")
                continue

        print("Invalid input. Please enter a number, 'm' for mixed game, or 'q' to quit.")

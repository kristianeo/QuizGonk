
from Views.quizzer import gameLoop

def mainMenu(data):
    games = data['games']
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
                    print(f"{i+1}. Game {i+1} ({game['questions']} questions)")
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
            gameLoop("m")
            return None

        if userInput.isdigit():
            index = int(userInput) -1
            if 0 <= index < len(games):
                gameLoop(userInput)
                return None
            else:
                print(f"Please select a number between 1 and {len(games)}.")
                continue

        print("Invalid input. Please enter a number, 'm' for mixed game, or 'q' to quit.")

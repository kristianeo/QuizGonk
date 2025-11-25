from tkinter import *

def mainMenu(root, handler):
    frame = Frame(root)
    # Load quiz summary if not already loaded
    handler._load_quiz_summary()

    games = handler.quiz_summary.get('games', [])
    handler.quiz_game_data = []

    if not games:
        label1 = Label(frame, text="No games available.", foreground='black', background='white')
        label1.pack(padx=20, pady=20)
    else:
        for i, game in enumerate(games):
            game_name = game.get('name', f'Game {i+1}')
            button1 = Button(handler.root, text=f"{i+1}. {game_name} ({game['questions']} questions)",
                             command=lambda: start_game(handler, i))
            button1.pack()
        total = handler.quiz_summary.get('total_questions', 0)
        mixed_count = min(15, total) if total > 0 else 15
        button2 = Button(frame, text=f"M. Mixed game ({mixed_count} random questions)",
                         command=lambda: start_mixed_game(handler))
        button2.pack()
    button_quit = Button(frame, text='Quit', command=handler.quit())
    button_quit.pack()
    return Frame


def start_mixed_game(handler):
    handler.selected_game = "m"
    handler.navigate_to("quiz")
    return

def start_game(handler, index):
    print(f'Button clicked, starting game {index}')
    handler.selected_game = index
    handler.navigate_to("quiz")
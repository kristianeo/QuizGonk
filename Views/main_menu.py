from view_handler import *

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Game",
            command=lambda: controller.show_frame(GameLoop),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

    def mainMenu(self):
        # Load quiz summary if not already loaded
        games = self.quiz_summary.get('games', [])
        self.quiz_game_data = []
        for i, game in enumerate(games):
            game_name = game.get('name', f'Game {i + 1}')
            print(f"{i + 1}. {game_name} ({game['questions']} questions)")
        total = handler.quiz_summary.get('total_questions', 0)
        mixed_count = min(15, total) if total > 0 else 15
        print(f"M. Mixed game ({mixed_count} random questions)")


    def start_mixed_game(handler):
        handler.selected_game = "m"
        handler.navigate_to("quiz")
        return


    def start_game(handler, index):
        print(f'Button clicked, starting game {index}')
        handler.selected_game = index
        handler.navigate_to("quiz")
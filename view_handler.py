import pymysql
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

# from Views.main_menu import mainMenu
# from Views.quizzer import game_loop
# from Views.results import show_results
# from Views.review import show_review

load_dotenv(".env")

class ViewHandler(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("QuizGonk")

        # Database connection settings
        self.db_config = {
            'host': os.environ.get("DB_ADDRESS"),
            'user': os.environ.get("PYTHON_DB_USER"),
            'passwd': os.environ.get("PYTHON_USER_PASSWORD"),
            'database': os.environ.get("DB_NAME")
        }

        self.quiz_summary = {
            "total_games": 0,
            "total_questions": 0,
        }
        self.quiz_game_data = []
        self.selected_game = None
        self.user_answers = []
        self.results_data = []
        self.review_data = []

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainMenu, GameLoop, ResultsScreen, ReviewScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainMenu)

    def _get_db_connection(self):
        return pymysql.connect(**self.db_config)

    def _load_quiz_summary(self):  # Bruker summary i main menu for å vise antall quizzer
        mydb = self._get_db_connection()
        cursor = mydb.cursor()

        cursor.execute("SELECT COUNT(*) FROM QuizzerQuestions.games")
        result = cursor.fetchone()
        total_games = result[0] if result else 0

        cursor.execute("SELECT COUNT(*) FROM QuizzerQuestions.questions")
        result = cursor.fetchone()
        total_questions = result[0] if result else 0

        cursor.execute("""
                       SELECT g.gameID, g.name, COUNT(q.questionID) as question_count
                       FROM QuizzerQuestions.games g
                                LEFT JOIN QuizzerQuestions.questions q ON g.gameID = q.gameID
                       GROUP BY g.gameID, g.name
                       ORDER BY g.gameID
                       """)
        games = cursor.fetchall()

        cursor.close()
        mydb.close()

        self.quiz_summary = {
            'total_games': total_games,
            'total_questions': total_questions,
            'games': [{'gameID': game[0], 'name': game[1], 'questions': game[2]} for game in games]
        }

    def _load_quiz_game_data(self):  # Laster inn spørsmål for valgt quiz
        selected_game = self.selected_game
        mydb = self._get_db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)

        if selected_game == "m":
            # Mixed
            cursor.execute("""
                           SELECT q.questionID, q.gameID, q.question, q.correct_answer, g.name as game_name
                           FROM QuizzerQuestions.questions q
                                    JOIN QuizzerQuestions.games g ON q.gameID = g.gameID
                           ORDER BY RAND()
                           LIMIT 15
                           """)
        else:
            # specific game
            cursor.execute("""
                           SELECT q.questionID, q.gameID, q.question, q.correct_answer, g.name as game_name
                           FROM QuizzerQuestions.questions q
                                    JOIN QuizzerQuestions.games g ON q.gameID = g.gameID
                           WHERE q.gameID = %s
                           ORDER BY q.questionID
                           """, (selected_game,))

        questions = cursor.fetchall()

        self.quiz_game_data = []
        for question in questions:
            cursor.execute("""
                           SELECT option_text, option_index
                           FROM QuizzerQuestions.options
                           WHERE questionID = %s
                           ORDER BY option_index
                           """, (question['questionID'],))

            options = cursor.fetchall()

            question_data = {
                'questionID': question['questionID'],
                'gameID': question['gameID'],
                'game_name': question['game_name'],
                'question': question['question'],
                'correct_answer': question['correct_answer'],
                'options': [opt['option_text'] for opt in options]
            }

            self.quiz_game_data.append(question_data)

        cursor.close()
        mydb.close()

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()




class GameLoop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Game")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Results Screen",
            command=lambda: controller.show_frame(ReviewScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class ResultsScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Results Screen")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Review Screen",
            command=lambda: controller.show_frame(ReviewScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class ReviewScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Review Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainMenu)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
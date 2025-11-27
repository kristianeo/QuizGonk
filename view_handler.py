import pymysql
from dotenv import load_dotenv
import os

load_dotenv(".env")

class ViewHandler:
    def __init__(self, term):
        self.term = term
        self.current_view = "main"

        #Database connection settings
        self.db_config = {
            'host': os.environ.get("DB_ADDRESS"),
            'user': os.environ.get("PYTHON_DB_USER"),
            'passwd': os.environ.get("PYTHON_USER_PASSWORD"),
            'database': os.environ.get("DB_NAME")
        }
        
        #Shared data across views
        self.quiz_summary = {
            "total_games": 0,
            "total_questions": 0,
        }
        self.quiz_game_data = []
        self.selected_game = None
        self.user_answers = []
        self.results_data = []
        self.review_data = []
        
        #flag to control the main loop
        self.running = True
    
    def _get_db_connection(self):
        return pymysql.connect(**self.db_config)
    
    def _load_quiz_summary(self): #Bruker summary i main menu for å vise antall quizzer
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
    
    def _load_quiz_game_data(self): #Laster inn spørsmål for valgt quiz
        selected_game = self.selected_game
        mydb = self._get_db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        
        if selected_game == "m":
            #Mixed
            cursor.execute("""
                SELECT q.questionID, q.gameID, q.question, q.correct_answer, g.name as game_name
                FROM QuizzerQuestions.questions q
                JOIN QuizzerQuestions.games g ON q.gameID = g.gameID
                ORDER BY RAND()
                LIMIT 15
            """)
        else:
            #specific game
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

    def navigate_to(self, view_name):
        self.current_view = view_name
    
    def quit(self):
        self.running = False
    
    def run(self):
        from Views.main_menu import mainMenu
        from Views.quizzer import game_loop
        from Views.results import show_results
        from Views.review import show_review
        from Views.credits import show_credits
        
        while self.running:
            if self.current_view == "main":
                mainMenu(self)
            elif self.current_view == "quiz":
                game_loop(self)
            elif self.current_view == "results":
                show_results(self)
            elif self.current_view == "review":
                show_review(self)
            elif self.current_view =='credits':
                show_credits(self)
            else:
                print(f"Unknown view: {self.current_view}")
                self.current_view = "main"

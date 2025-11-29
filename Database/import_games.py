import pymysql
import json
from dotenv import load_dotenv
import os
from pathlib import Path

json_path = Path(__file__).parents[1] / 'Database/questions.json'


def import_games():
    print("Starting import of games...")
    load_dotenv("../.env")

    if not json_path.exists():
        print(f"ERROR: Could not find questions.json at {json_path}")
        print("Please ensure the file exists before running the application.")
        return False

    try:
        mydb = pymysql.connect(
            host = os.environ.get("DB_ADDRESS"),
            user = os.environ.get("PYTHON_DB_USER"),
            passwd = os.environ.get("PYTHON_USER_PASSWORD"),
            database = os.environ.get("DB_NAME")
        )
    except pymysql.Error as e:
        print(f"ERROR: Failed to connect to database: {e}")
        print("Please check your database connection settings in .env file.")
        return False

    try:
        with open(json_path, 'r') as qj:
            data = json.load(qj)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON format in questions.json: {e}")
        mydb.close()
        return False
    except Exception as e:
        print(f"ERROR: Failed to read questions.json: {e}")
        mydb.close()
        return False

    print(f"Loaded {len(data['games'])} games from questions.json")

    try:
        cursor = mydb.cursor()

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE QuizzerQuestions.options")
        cursor.execute("TRUNCATE TABLE QuizzerQuestions.questions")
        cursor.execute("TRUNCATE TABLE QuizzerQuestions.games")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        game_number = 0
        for game in data["games"]:
            game_number += 1
            print(f"Processing game {game_number}...")
            cursor.execute("INSERT INTO QuizzerQuestions.games(name) VALUES (%s)",
                           f'Game {game_number}', )
            game_id = cursor.lastrowid

            for q in game["questions"]:
                cursor.execute("INSERT INTO QuizzerQuestions.questions(gameID, question, correct_answer) VALUES (%s, %s, %s)",
                               (game_id, q["question"], q["correct"])
                               )
                question_id = cursor.lastrowid

                for index, option_text in enumerate(q["content"]):
                    cursor.execute("INSERT INTO QuizzerQuestions.options(questionID, option_text, option_index) VALUES (%s, %s, %s)",
                                   (question_id, option_text, index)
                                   )

        mydb.commit()
        cursor.close()
        mydb.close()
        print("Import completed successfully!")
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
        
    except pymysql.Error as e:
        print(f"ERROR: Database operation failed: {e}")
        mydb.rollback()
        mydb.close()
        return False
    except KeyError as e:
        print(f"ERROR: Invalid JSON structure, missing key: {e}")
        mydb.close()
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error during import: {e}")
        mydb.close()
        return False
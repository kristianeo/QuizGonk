from Views.main_menu import mainMenu
from Database.import_games import importGames
from pathlib import Path
import pymysql
from dotenv import load_dotenv
import os


def getGames():
    load_dotenv("../.env")

    mydb = pymysql.connect(
        host = os.environ.get("DB_ADDRESS"),
        user = os.environ.get("PYTHON_DB_USER"),
        passwd = os.environ.get("PYTHON_USER_PASSWORD"),
        database = os.environ.get("DB_NAME")
        )

    cursor = mydb.cursor()

    cursor.execute("SELECT COUNT(*) FROM QuizzerQuestions.games")
    result = cursor.fetchone()
    total_games = result[0] if result else 0

    cursor.execute("""
        SELECT g.gameID, COUNT(q.questionID) as question_count
        FROM QuizzerQuestions.games g
        LEFT JOIN QuizzerQuestions.questions q ON g.gameID = q.gameID
        GROUP BY g.gameID
        ORDER BY g.gameID
    """)
    games = cursor.fetchall()

    cursor.close()
    mydb.close()

    return {
        'total_games': total_games,
        'games': [{'questions': game[1]} for game in games]
    }

if __name__ == "__main__":
    importGames()
    games = getGames()
    mainMenu(games)
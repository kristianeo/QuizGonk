import pymysql #Python library for MySQL queries
import json
from dotenv import load_dotenv
import os

load_dotenv("../.env")

mydb = pymysql.connect(
    host = os.environ.get("DB_ADDRESS"),
    user = os.environ.get("PYTHON_DB_USER"),
    passwd = os.environ.get("PYTHON_USER_PASSWORD"),
    database = os.environ.get("DB_NAME")
    )

with (open('questions.json', 'r') as qj):
    data = json.load(qj)

cursor = mydb.cursor()

game_number = 0
for i in data["games"]:
    game_number += 1
    cursor.execute("INSERT INTO QuizzerQuestions.games(name) VALUES (%s)",
                   f'Game {game_number}',)

mydb.commit()
cursor.close()
mydb.close()
from collections import defaultdict
from Database.import_games import *

load_dotenv("../.env")

mydb = pymysql.connect(
    host = os.environ.get("DB_ADDRESS"),
    user = os.environ.get("PYTHON_DB_USER"),
    passwd = os.environ.get("PYTHON_USER_PASSWORD"),
    database = os.environ.get("DB_NAME")
    )

with (open('Database/questions.json', 'r') as qj):
    data = json.load(qj)
def game_loop(selected):
    global selected_index
    selected_game = selected
    print("Let's test your knowledge!")
    cursor = mydb.cursor()
    query = """
            SELECT option_text, options.questionID
            FROM QuizzerQuestions.options
                     JOIN QuizzerQuestions.questions ON options.questionID = questions.questionID
            WHERE gameID = %s
            """
    cursor.execute(query, (selected_game,))
    alternatives = cursor.fetchall()
    cursor.close()

    alt_list = defaultdict(list)
    for k, v in alternatives:
        alt_list[v].append(k)
    alt_list2 = list(alt_list.values())

    cursor = mydb.cursor()
    query = """
            SELECT question, correct_answer, questionID
            FROM QuizzerQuestions.questions
            WHERE gameID = %s
            """
    cursor.execute(query, (selected_game,))
    question = cursor.fetchall()
    cursor.close()

    quest_list = []
    for q in question:
        quest_list.append(list(q))

    right_wrong = []
    answers = []
    correct = []
    question_number = 0
    for (a, b, c), d in zip(quest_list, alt_list2):
        correct.append(b)
        print(f"Question {question_number+1}: {a}")
        for i, j in enumerate(d, 1):
            print(f"{i}. {j}")
        question_number += 1

        selected_index = int(input("Choose an answer: "))-1
        answers.append(selected_index)

        if selected_index == b:
            right_wrong.append("right")
            print(right_wrong)
        else:
            right_wrong.append("wrong")
            print(right_wrong)
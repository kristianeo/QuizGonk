from collections import defaultdict

from Database.import_games import *
load_dotenv("../.env")

mydb = pymysql.connect(
    host = os.environ.get("DB_ADDRESS"),
    user = os.environ.get("PYTHON_DB_USER"),
    passwd = os.environ.get("PYTHON_USER_PASSWORD"),
    database = os.environ.get("DB_NAME")
    )

with (open('questions.json', 'r') as qj):
    data = json.load(qj)

def get_question_list(selected_game, mydb):
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

    cursor = mydb.cursor()
    query = """
            SELECT question, correct_answer, questionID
            FROM QuizzerQuestions.questions
            WHERE gameID = %s
            """
    cursor.execute(query, (selected_game,))
    questions = cursor.fetchall()
    cursor.close()

    quest_list = defaultdict(list)
    right_index_list = defaultdict(list)
    for q, r, s in questions:
        quest_list[s].append(q)
        right_index_list[s].append(r)

    final_list = defaultdict(list)
    for x in (quest_list, right_index_list, alt_list):
        for key, value in x.items():
            final_list[key].append(value)

    print(list(final_list.values()))
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
#
# def get_question_list(selected_game, mydb):
#     cursor = mydb.cursor()
#     query = """
#             SELECT option_text, options.questionID
#             FROM QuizzerQuestions.options
#                      JOIN QuizzerQuestions.questions ON options.questionID = questions.questionID
#             WHERE gameID = %s
#             """
#     cursor.execute(query, (selected_game,))
#     alternatives = cursor.fetchall()
#     cursor.close()
#
#     alt_list = defaultdict(list)
#     for k, v in alternatives:
#         alt_list[v].append(k)
#
#     cursor = mydb.cursor()
#     query = """
#             SELECT question, correct_answer, questionID
#             FROM QuizzerQuestions.questions
#             WHERE gameID = %s
#             """
#     cursor.execute(query, (selected_game,))
#     question = cursor.fetchall()
#     cursor.close()
#
#     quest_list = defaultdict(list)
#     right_index_list = defaultdict(list)
#     for q, r, s in question:
#         quest_list[s].append(q)
#         right_index_list[s].append(r)
#
#     final_list = defaultdict(list)
#     for x in (quest_list, right_index_list, alt_list):
#         for key, value in x.items():
#             final_list[key].append(value)
#
#     print(list(final_list.values()))
#     questions = list(final_list.values())
#     return questions

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
    print(list(alt_list.values()))
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
    right_index_list = []
    for q in question:
        quest_list.append(list(q))
    print(quest_list)
    # print(right_index_list)

    # final_list = defaultdict(list)
    # for x in (quest_list, right_index_list, alt_list):
    #     for key, value in x.items():
    #         final_list[key].append(value)

    # print(list(final_list.values()))
    # questions = list(final_list.values())

    right_wrong = []
    answers = []
    correct = []
    question_number = 0
    for (a, b, c), d in zip(quest_list, alt_list2):
        correct.append(b)
        print(f"Correct answers: {correct}")
        print(f"Question {question_number+1}: {a}")
        for i, j in enumerate(d, 1):
            print(f"{i}. {j}")
        question_number += 1

        selected_index = int(input("Choose an answer: "))-1
        answers.append(selected_index)
        print(f"answers: {answers}")

        if selected_index == c:
            right_wrong.append("right")
            print(right_wrong)
        else:
            right_wrong.append("wrong")
            print(right_wrong)



game_loop(3)

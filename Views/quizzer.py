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

def get_questions(selected_game, mydb):
    cursor = mydb.cursor()
    query = """
            SELECT question, correct_answer
            FROM QuizzerQuestions.questions
            WHERE gameID = %s
            """
    cursor.execute(query, (selected_game,))
    questions = cursor.fetchall()
    cursor.close()
    q_and_right_answer = []
    for q in questions:
        q_and_right_answer.append(q)
    print(q_and_right_answer)

def get_alternatives(selected_game, mydb):
    cursor = mydb.cursor()
    query = """
            SELECT option_text, option_index
            FROM QuizzerQuestions.options
            JOIN QuizzerQuestions.questions ON options.questionID = questions.questionID
            WHERE gameID = %s
            """
    cursor.execute(query, (selected_game,))
    alternatives = cursor.fetchall()
    alternatives_and_indices = []
    cursor.close()
    for a in alternatives:
        alternatives_and_indices.append(a)
    print(alternatives_and_indices)

def game_loop(selected):
    selected_game = selected
    print("Let's test your knowledge!")
    get_questions(selected_game, mydb)
    get_alternatives(selected_game, mydb)

#
#
# right_wrong = []
# answers = []

game_loop(3)



    #Get selected game
    #getQuestions(selected_game)
        #Returns questions
    #getAlternatives()
    #getCorrectIDX()
    ### Questions =[[spørsmål1,[alt1, alt2, alt3, alt4],[2]], Spørsmål2, [Alternativer],[riktig svar] ]
    #answers = []
    # right_wrong = ["right", "wrong", "right", "wrong"]
    #
    # for each question in questions():
        # correct.append(question[1])
        # print(question[0])
        #   for each alt in question[1]
        # selected_answer_idx = int(input("Velg et svar"))-1
        # answers.append(selected_answer_idx)
        # if selected_answer_idx == question[2]:
        # right_wrong.append("right")
        # else right_wrong.append("wrong")
    #resultScreen(selected_game, answers, correct)
    #valid inputs xX/ qQ for quit, 1-4 for svar
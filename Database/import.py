import mysql.connector
import json
from dotenv import dotenv_values
config = dotenv_values(".env")

mydb = mysql.connector.connect(
    host = config['DB_ADDRESS'],
    user = config['PYTHON_DB_USER'],
    passwd = config['PYTHON_USER_PASSWORD'],
    database = config['DB_NAME']
)

with (open('questions.json', 'r') as qj):
    data = json.load(qj)
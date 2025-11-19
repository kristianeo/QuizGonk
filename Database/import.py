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

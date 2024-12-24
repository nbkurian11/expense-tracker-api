from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def make_db():
    connection = sqlite3.connect('expenses.db')

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE expenses(
               accountno INTEGER PRIMARY KEY
               date TEXT,
               type TEXT,
               amount REAL,
               description TEXT)""")

    connection.commit()

    connection.close()

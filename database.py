import sqlite3
from flask import Flask

def create_app():
    app = Flask(__name__)
    conn = sqlite3.connect('daam.db')

    return app
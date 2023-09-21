"""
Handling SQlite database

log
- lid
- word
- uid
- time
- points

Words
- wid
- word
- def
- time
- points

"""

import sqlite3
from datetime import datetime
import pandas as pd

db_path = "Qwordy/qdb.db"

def sq_conn():
    conn = sqlite3.connect(db_path)
    return conn

def insert_guess(data):
    conn = sq_conn()
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO log (word, uid, time, points) VALUES (?, ?, ?, ?)
    """
    cursor.execute(insert_query, data)
    conn.commit()

def insert_word(data):
    conn = sq_conn()
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Words (word, def, time, points) VALUES (?, ?, ?, ?)
    """
    cursor.execute(insert_query, data)
    conn.commit()


def get_day_words():
    conn = sqlite3.connect(db_path)
    day = datetime.now().date()
    query = "SELECT word, def, points FROM Words WHERE DATE(time) = ?"
    df = pd.read_sql_query(query, conn, params=(day,))
    df = df.set_index("word")
    ddf = df.to_dict(orient='index')
    return ddf

def get_max_points():
    conn = sqlite3.connect(db_path)
    day = datetime.now().date()
    query = "SELECT SUM(points) FROM Words WHERE DATE(time) = ?"
    df = pd.read_sql_query(query, conn, params=(day,))
    max_p = df.values[0][0]

    query = "SELECT COUNT(*) FROM Words WHERE DATE(time) = ?"
    df = pd.read_sql_query(query, conn, params=(day,))
    max_w = df.values[0][0]

    return max_p, max_w



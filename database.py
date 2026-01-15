# database.py
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS documents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            language TEXT,
            category TEXT,
            keywords TEXT,
            summary TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS audio_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_type TEXT,
            language TEXT,
            filename TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_document(f, l, c, k, s):
    sqlite3.connect("data.db").execute(
        "INSERT INTO documents VALUES(NULL,?,?,?,?,?)",
        (f, l, c, k, s)
    ).connection.commit()

def save_audio(ct, l, f):
    sqlite3.connect("data.db").execute(
        "INSERT INTO audio_history VALUES(NULL,?,?,?,?)",
        (ct, l, f, datetime.now())
    ).connection.commit()

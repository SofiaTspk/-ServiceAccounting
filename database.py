# client_management_system/database.py
import sqlite3

DB_NAME = 'clients.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                services TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_connection():
    return sqlite3.connect(DB_NAME)

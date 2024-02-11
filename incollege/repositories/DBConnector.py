# Global Database Connection Handler
# Creates global single database connection to avoid repeat connections from individual repositories

import sqlite3
import incollege.config.Config as Config

conn = None


def get_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect(Config.DATABASE_NAME, check_same_thread=False)
    return conn


def close_connection():
    conn.close()


def create_tables():
    cursor = get_connection().cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS auth (
            username TEXT,
            password_hash TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            title TEXT,
            desc TEXT, 
            employer TEXT,
            location TEXT, 
            salary REAL
        )
    ''')
    
    conn.commit()

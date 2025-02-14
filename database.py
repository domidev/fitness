import sqlite3

def create_database():
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS workouts
                (id INTEGER PRIMARY KEY, date TEXT, type TEXT, duration INTEGER, calories INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS meals
                (id INTEGER PRIMARY KEY, date TEXT, name TEXT, calories INTEGER, protein INTEGER, carbs INTEGER, fat INTEGER)''')
    conn.commit()
    conn.close()
# scripts/init_sample_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("data/sample.db")
    cursor = conn.cursor()

    with open("scripts/init_sample_db.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("sample.db initialized with tables and data.")

if __name__ == "__main__":
    init_db()

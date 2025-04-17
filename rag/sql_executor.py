## rag/sql_executor.py
import sqlite3
import sqlglot

DB_PATH = "data/sample.db"

def is_query_safe(sql: str) -> bool:
    try:
        parsed = sqlglot.parse_one(sql)
        return parsed.sql().strip().upper().startswith("SELECT")
    except Exception:
        return False

def execute_sql(sql: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    conn.close()
    return colnames, rows

def explain_sql(sql: str, openai_chat_fn) -> str:
    prompt = f"Explain this SQL query in plain English:\n\n{sql}"
    return openai_chat_fn(prompt)
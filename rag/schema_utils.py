## schema_utils.py
import sqlite3
from typing import List

def extract_schema(db_path: str) -> List[str]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema_chunks = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for (table_name,) in tables:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()  # [(cid, name, type, notnull, default, pk), ...]

        col_defs = [f"{col[1]} ({col[2]})" for col in columns]
        chunk = f"Table: {table_name}\nColumns: {', '.join(col_defs)}"
        schema_chunks.append(chunk)

    conn.close()
    return schema_chunks
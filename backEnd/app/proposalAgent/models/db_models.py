import sqlite3

DB_NAME = "app.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS proposals (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   prospect_name TEXT,
                   company_name TEXT,
                   prospect_url TEXT,
                   call_notes TEXT,
                   title TEXT,
                   description TEXT,
                   budget REAL,
                   additional_context TEXT,
                   status TEXT,
                   parsed_data TEXT,
                   research_data TEXT,
                   retrieved_context TEXT,
                   sections TEXT,
                   review TEXT,
                   error_message TEXT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                   """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS knowledge_docs (
                   id TEXT PRIMARY KEY,
                   filename TEXT,
                   original_path TEXT,
                   collection_name TEXT,
                   chunk_count INTEGER,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                   """
    )
    conn.commit()
    conn.close()

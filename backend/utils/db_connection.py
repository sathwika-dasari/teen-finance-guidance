import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema_path = os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

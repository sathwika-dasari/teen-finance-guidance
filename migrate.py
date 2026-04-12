import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'backend', 'database.db')

def migrate():
    # If the database doesn't exist, create it from schema.sql
    if not os.path.exists(DB_PATH):
        print(f"Database not found. Initialising from schema.sql...")
        schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
        if not os.path.exists(schema_path):
             # Try parent directory if running from backend/ or somewhere else
             schema_path = os.path.join(os.getcwd(), 'database', 'schema.sql')
        
        if os.path.exists(schema_path):
            conn = sqlite3.connect(DB_PATH)
            with open(schema_path, 'r') as f:
                conn.executescript(f.read())
            conn.commit()
            conn.close()
            print("Database created and base schema applied.")
        else:
            print("ERROR: Could not find schema.sql to initialize database.")
            return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Checking for additional migrations...")

    # Add email column to users
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")
        print("Added 'email' column to 'users' table.")
    except sqlite3.OperationalError:
        print("'email' column already exists.")

    # Add user_difficulty column to users
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN user_difficulty TEXT DEFAULT 'easy'")
        print("Added 'user_difficulty' column to 'users' table.")
    except sqlite3.OperationalError:
        print("'user_difficulty' column already exists.")

    # Add role column to users
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'student'")
        print("Added 'role' column to 'users' table.")
    except sqlite3.OperationalError:
        print("'role' column already exists.")

    # Create guardian_links table
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guardian_links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guardian_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (guardian_id) REFERENCES users (id),
                FOREIGN KEY (student_id) REFERENCES users (id),
                UNIQUE(guardian_id, student_id)
            )
        """)
        print("Created 'guardian_links' table.")
    except Exception as e:
        print(f"Error creating 'guardian_links' table: {e}")

    conn.commit()
    conn.close()
    print("Migration complete.")

if __name__ == "__main__":
    migrate()

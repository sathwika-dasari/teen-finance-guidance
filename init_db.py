import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from backend.utils.db_connection import init_db

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")

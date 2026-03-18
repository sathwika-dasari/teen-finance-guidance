from ..utils.db_connection import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    @staticmethod
    def create_user(username, password, age, skills):
        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password_hash, age, skills) VALUES (?, ?, ?, ?)',
                (username, password_hash, age, skills)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def get_user_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def update_user(user_id, age=None, skills=None):
        conn = get_db_connection()
        try:
            if age:
                conn.execute('UPDATE users SET age = ? WHERE id = ?', (int(age), user_id))
            if skills:
                conn.execute('UPDATE users SET skills = ? WHERE id = ?', (skills, user_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            conn.close()
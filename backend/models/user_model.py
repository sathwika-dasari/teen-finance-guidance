from ..utils.db_connection import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    @staticmethod
    def create_user(username, password, email, age, skills, role='student'):
        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password_hash, email, age, skills, role) VALUES (?, ?, ?, ?, ?, ?)',
                (username, password_hash, email, age, skills, role)
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
        return dict(user) if user else None

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def link_guardian(guardian_id, student_email):
        conn = get_db_connection()
        try:
            # Find the student
            student = conn.execute('SELECT id FROM users WHERE email = ? AND role = "student"', (student_email,)).fetchone()
            if not student:
                return False, "Student with that email not found."
            
            # Create link
            conn.execute(
                'INSERT OR IGNORE INTO guardian_links (guardian_id, student_id) VALUES (?, ?)',
                (guardian_id, student['id'])
            )
            conn.commit()
            return True, "Successfully linked!"
        except Exception as e:
            print(f"Error linking guardian: {e}")
            return False, "Database error."
        finally:
            conn.close()

    @staticmethod
    def get_linked_students(guardian_id):
        conn = get_db_connection()
        query = """
            SELECT u.id, u.username, u.email, u.age, u.skills, u.user_difficulty,
                   g.xp, g.current_streak
            FROM users u
            JOIN guardian_links l ON u.id = l.student_id
            LEFT JOIN gamification g ON u.id = g.user_id
            WHERE l.guardian_id = ?
        """
        students = conn.execute(query, (guardian_id,)).fetchall()
        
        # Convert to list of dicts for JSON serialization
        results = []
        for s in students:
            res = dict(s)
            # Add progress stats
            progress = conn.execute('SELECT module_name, status, score FROM progress WHERE user_id = ?', (s['id'],)).fetchall()
            res['progress'] = [dict(p) for p in progress]
            results.append(res)
            
        conn.close()
        return results

    @staticmethod
    def get_user_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return dict(user) if user else None

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
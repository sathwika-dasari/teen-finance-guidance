from ..utils.db_connection import get_db_connection

class ProgressModel:
    @staticmethod
    def update_progress(user_id, module_name, status, score=0):
        conn = get_db_connection()
        existing = conn.execute(
            'SELECT id FROM progress WHERE user_id = ? AND module_name = ?',
            (user_id, module_name)
        ).fetchone()

        if existing:
            conn.execute(
                'UPDATE progress SET status = ?, score = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
                (status, score, existing['id'])
            )
        else:
            conn.execute(
                'INSERT INTO progress (user_id, module_name, status, score) VALUES (?, ?, ?, ?)',
                (user_id, module_name, status, score)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def get_user_progress(user_id):
        conn = get_db_connection()
        progress = conn.execute('SELECT * FROM progress WHERE user_id = ?', (user_id,)).fetchall()
        conn.close()
        return [dict(p) for p in progress]

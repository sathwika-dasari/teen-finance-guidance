from ..utils.db_connection import get_db_connection
from datetime import datetime, date

class GamificationModel:
    @staticmethod
    def get_user_stats(user_id):
        conn = get_db_connection()
        stats = conn.execute('SELECT * FROM gamification WHERE user_id = ?', (user_id,)).fetchone()
        
        if not stats:
            conn.execute('INSERT INTO gamification (user_id, xp, current_streak, last_active) VALUES (?, 0, 0, ?)', (user_id, None))
            conn.commit()
            stats = conn.execute('SELECT * FROM gamification WHERE user_id = ?', (user_id,)).fetchone()
            
        conn.close()
        return dict(stats)

    @staticmethod
    def add_xp_and_update_streak(user_id, xp_amount):
        conn = get_db_connection()
        stats = conn.execute('SELECT * FROM gamification WHERE user_id = ?', (user_id,)).fetchone()
        
        today = date.today().isoformat()
        
        if not stats:
            conn.execute('INSERT INTO gamification (user_id, xp, current_streak, last_active) VALUES (?, ?, 1, ?)', (user_id, xp_amount, today))
            conn.commit()
            stats = conn.execute('SELECT * FROM gamification WHERE user_id = ?', (user_id,)).fetchone()
        else:
            last_active = stats['last_active']
            current_streak = stats['current_streak']
            new_xp = stats['xp'] + xp_amount
            
            if last_active == today:
                # Already active today, just add XP
                new_streak = current_streak
            else:
                # Check if it was yesterday
                try:
                    if last_active:
                        last_active_date = datetime.strptime(last_active, '%Y-%m-%d').date()
                        if (date.today() - last_active_date).days == 1:
                            new_streak = current_streak + 1
                        else:
                            new_streak = 1
                    else:
                        new_streak = 1
                except:
                    new_streak = 1
            
            conn.execute('UPDATE gamification SET xp = ?, current_streak = ?, last_active = ? WHERE user_id = ?', 
                        (new_xp, new_streak, today, user_id))
            conn.commit()
            
        conn.close()
        return GamificationModel.get_user_stats(user_id)

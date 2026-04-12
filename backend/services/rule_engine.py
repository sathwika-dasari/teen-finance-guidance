from ..utils.db_connection import get_db_connection

class RuleEngine:
    @staticmethod
    def get_user_difficulty(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT user_difficulty FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user['user_difficulty'] if user else 'easy'

    @staticmethod
    def update_difficulty(user_id, is_correct, current_session_stats):
        """
        Adaptive difficulty logic:
        - 3 consecutive correct -> 'hard'
        - 2 wrong (in a row or total in session?) -> 'easy'
        
        The user specified: "if a user answers 3 consecutive questions correctly, increase difficulty to 'hard'; if they answer 2 wrong, drop to 'easy'."
        """
        conn = get_db_connection()
        user = conn.execute('SELECT user_difficulty FROM users WHERE id = ?', (user_id,)).fetchone()
        if not user:
            conn.close()
            return 'easy'
            
        current_diff = user['user_difficulty']
        new_diff = current_diff

        # We need to track consecutive correct/wrong. 
        # Since this is a service, we'll assume session_stats is passed or we use a temporary session store.
        # For simplicity, let's just use the session_stats passed from the route.
        
        consecutive_correct = current_session_stats.get('consecutive_correct', 0)
        total_wrong = current_session_stats.get('total_wrong', 0)

        if is_correct:
            consecutive_correct += 1
            if consecutive_correct >= 3:
                new_diff = 'hard'
        else:
            consecutive_correct = 0
            total_wrong += 1
            if total_wrong >= 2:
                new_diff = 'easy'

        if new_diff != current_diff:
            conn.execute('UPDATE users SET user_difficulty = ? WHERE id = ?', (new_diff, user_id))
            conn.commit()
            
        conn.close()
        return new_diff, consecutive_correct, total_wrong

    @staticmethod
    def get_recommendations(age, skills, difficulty='easy'):
        recommendations = {
            "lessons": [],
            "guidance": [],
            "title": "",
            "difficulty": difficulty
        }

        try:
            age = int(age)
        except (ValueError, TypeError):
            age = 0

        if age < 18:
            recommendations["title"] = "Financial Literacy for Teens"
            recommendations["lessons"] = [
                {"id": "intro_finance", "title": "Basics of Finance", "desc": "Understanding money, savings, and value."},
                {"id": "scam_prevention", "title": "Scam Prevention", "desc": "How to stay safe online and avoid modern scams."},
                {"id": "budgeting_101", "title": "Intro to Budgeting", "desc": "Managing your pocket money effectively."}
            ]
        else:
            recommendations["title"] = "Advanced Financial Planning"
            recommendations["lessons"] = [
                {"id": "investing_stocks", "title": "Deep Dive: Stocks", "desc": "Learn how the stock market works and long-term investing."},
                {"id": "advanced_budgeting", "title": "Mastering Budgeting", "desc": "Wealth building through strategic budgeting."},
                {"id": "taxation_basics", "title": "Adulting: Tax & Finance", "desc": "Everything you need to know about taxes."}
            ]
            
            # Skills-based guidance
            from .career_content import CAREER_DATA
            
            skills_list = [s.strip().lower() for s in skills.split(',')]
            matched_ids = []
            
            if 'coding' in skills_list or 'programming' in skills_list:
                matched_ids.append("freelance_dev")
            
            if 'design' in skills_list or 'art' in skills_list:
                matched_ids.append("graphic_design")
                
            if 'writing' in skills_list or 'editing' in skills_list:
                matched_ids.append("content_writing")

            if 'teaching' in skills_list or 'tutoring' in skills_list:
                matched_ids.append("online_tutor")

            if 'marketing' in skills_list or 'social' in skills_list:
                matched_ids.append("social_media_manager")
            
            if not matched_ids:
                matched_ids.append("virtual_assistant")

            for cid in matched_ids:
                if cid in CAREER_DATA:
                    data = CAREER_DATA[cid].copy()
                    data["id"] = cid
                    recommendations["guidance"].append(data)

        return recommendations

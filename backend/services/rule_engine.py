class RuleEngine:
    @staticmethod
    def get_recommendations(age, skills):
        recommendations = {
            "lessons": [],
            "guidance": [],
            "title": ""
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

class RuleEngine:
    @staticmethod
    def get_recommendations(age, skills):
        recommendations = {
            "lessons": [],
            "guidance": [],
            "title": ""
        }

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
            skills_list = [s.strip().lower() for s in skills.split(',')]
            
            if 'coding' in skills_list or 'programming' in skills_list:
                recommendations["guidance"].append({"id": "freelance_dev", "title": "Freelance Web Development", "desc": "Start earning by building websites for local businesses."})
            
            if 'design' in skills_list or 'art' in skills_list:
                recommendations["guidance"].append({"id": "graphic_design", "title": "Graphic Design Gigs", "desc": "Monetize your creative skills on platforms like Upwork."})
                
            if 'writing' in skills_list or 'editing' in skills_list:
                recommendations["guidance"].append({"id": "content_writing", "title": "Content Writing", "desc": "Write articles and blogs to build your portfolio and income."})
            
            if not recommendations["guidance"]:
                recommendations["guidance"].append({"id": "general_freelance", "title": "Virtual Assistant", "desc": "High demand for general organizational and administrative support."})

        return recommendations

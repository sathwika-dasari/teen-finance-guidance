# Teen Finance Guidance Platform

A personalized financial literacy web application designed to help teenagers and young adults learn about finance, budgeting, investing, and earning money through interactive lessons, quizzes, and guided learning experiences.

---

## Overview

Teen Finance Guidance is a full-stack web application built with Flask and vanilla JavaScript. The platform delivers personalized financial education content based on the user's age and skills. Younger users receive foundational finance lessons while older users are guided toward advanced financial planning and part-time income opportunities.

---

## Features

- User authentication with secure password hashing
- Personalized lesson content based on user age and profile
- Interactive topic-based lessons with expandable sections
- Quiz system to test knowledge after each lesson
- Scam detection game built into the Scam Prevention lesson
- Progress tracking dashboard with a completion chart
- Seven-day streak tracker to encourage daily learning
- Badge system that rewards learning milestones
- Part-time career guidance with step-by-step roadmaps for users aged 18 and above
- Daily practice quiz with rotating questions
- AI-powered finance assistant chatbot using the Gemini API
- Profile management allowing users to update their age and skills

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | HTML, CSS, JavaScript             |
| Backend    | Python, Flask                     |
| Database   | SQLite                            |
| AI Chatbot | Google Gemini API                 |
| Icons      | Font Awesome                      |
| Charts     | Chart.js                          |

---

## Project Structure
```
teen-finance-guidance/
│
├── backend/
│   ├── app.py                  # Main Flask application
│   ├── config.py               # Application configuration
│   ├── database.db             # SQLite database
│   │
│   ├── models/
│   │   ├── user_model.py       # User table and methods
│   │   └── progress_model.py   # Learning progress table
│   │
│   ├── routes/
│   │   ├── auth_routes.py      # Authentication and profile APIs
│   │   ├── recommendation.py   # Lesson recommendation API
│   │   └── dashboard_routes.py # Progress dashboard APIs
│   │
│   ├── services/
│   │   └── rule_engine.py      # Rule-based recommendation logic
│   │
│   └── utils/
│       └── db_connection.py    # SQLite connection handler
│
├── frontend/
│   ├── screens/
│   │   ├── login.html          # Login and registration page
│   │   ├── home.html           # Home page
│   │   ├── lessons.html        # Lesson viewer and quiz
│   │   ├── dashboard.html      # Progress dashboard
│   │   ├── profile.html        # User profile and badges
│   │   ├── daily_practice.html # Daily quiz
│   │   └── parttime.html       # Part-time career guidance
│   │
│   ├── css/
│   │   └── style.css           # Global stylesheet
│   │
│   └── js/
│       └── api.js              # API communication layer
│
├── database/
│   └── schema.sql              # Database schema
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Installation and Setup

### Step 1 - Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/teen-finance-guidance.git
cd teen-finance-guidance
```

### Step 2 - Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 3 - Set up the database
```bash
python -m backend.init_db
```

### Step 4 - Configure the Gemini API key

Open `frontend/screens/home.html` and replace the placeholder with your API key obtained from Google AI Studio.
```javascript
const GEMINI_API_KEY = 'YOUR_API_KEY_HERE';
```

### Step 5 - Start the Flask server
```bash
python -m backend.app
```

### Step 6 - Open the application in your browser
```
http://localhost:5000/screens/login.html
```

---

## Pages Overview

| Page              | Description                                              |
|-------------------|----------------------------------------------------------|
| Login / Register  | Account creation and login                               |
| Home              | Dashboard with streak tracker, modules, and daily quiz   |
| Lessons           | Topic lessons with accordion content and quiz            |
| Scam Detective    | Interactive scam identification game                     |
| Dashboard         | Progress chart and lesson completion overview            |
| Profile           | User information, earned badges, and profile update      |
| Daily Practice    | Ten rotating daily finance questions                     |
| Part-Time Guidance| Career recommendations and roadmaps for users aged 18 plus|

---

## Security Notes

Passwords are stored as hashed values using the Werkzeug library. User sessions are managed server-side through Flask. The Gemini API key should never be committed to version control. The .gitignore file is configured to exclude the database file and any environment variable files.

---

## License

This project was built for educational purposes.

---

## Author

Developed as a financial literacy platform for teenagers and young adults.

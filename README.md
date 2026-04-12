# Teen Finance Guidance Platform

A personalized financial literacy web application designed to help teenagers and young adults learn about finance, budgeting, investing, and earning money through interactive lessons, quizzes, and guided learning experiences.

---

## 🌟 Key Features

- **Adaptive Learning Path**: Rule-based difficulty engine that adjusts content (Easy/Hard) based on user quiz performance.
- **Interactive Budget Simulator**: Visualize wealth projection with real-time Chart.js charts and monthly variables.
- **Scam Detective Game**: Expanded with 5+ India-specific scenarios (UPI fraud, Remote Access, etc.) and educational feedback.
- **Guardian Dashboard**: New role-based interface allowing parents/guardians to link to students and monitor Progress (XP, Streaks, Module Scores).
- **Proactive Security**: 
    - Moved Gemini AI to a secure backend proxy (`/api/chat`).
    - Full **CSRF Protection** via Flask-WTF.
    - Rate limiting on sensitive endpoints.
    - SQLite **WAL Mode** for high-performance concurrent database access.
- **Gamification**: XP system, 7-day streaks, and badge rewards.
- **AI-Powered Discovery**: Personalized job and internship recommendations using Google Gemini.

---

## 🚀 Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | HTML5, Vanilla CSS, JavaScript (ES6+) |
| Backend    | Python, Flask                     |
| Database   | SQLite (WAL Mode enabled)         |
| Core APIs  | Google Gemini AI (Backend Proxy)  |
| Libraries  | Chart.js, Font Awesome, Flask-WTF |

---

## 📁 Project Structure
```
teen-finance-guidance/
├── backend/
│   ├── app.py                  # Main Flask app & route registry
│   ├── config.py               # Security & DB configurations
│   ├── database.db             # SQLite DB (WAL Mode)
│   ├── models/                 # UserModel, Progress, Gamification
│   ├── routes/                 # Auth, Learning, Chat (Proxy), Jobs
│   ├── services/               # RuleEngine, LessonContent
│   └── utils/                  # DB Connection with WAL init
├── frontend/
│   ├── screens/                # All UI pages (Dashboard, Guardian, etc.)
│   ├── css/                    # Glassmorphism & Modern UI styling
│   └── js/                     # API utility with CSRF handling
├── database/                   # Schema.sql & migrations
├── .env.example                # Template for secrets
└── README.md                   # You are here
```

---

## 🛠️ Installation and Setup

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/teen-finance-guidance.git
cd teen-finance-guidance
pip install -r requirements.txt
```

### 2. Configure Environment
Rename `.env.example` to `.env` and add your **GEMINI_API_KEY**.
```env
GEMINI_API_KEY=your_key_here
FLASK_SECRET_KEY=your_random_secret
```

### 3. Initialize Database
```bash
# Run migration script to set up tables and WAL mode
python migrate.py
```

### 4. Run the Dev Server
```bash
python -m backend.app
```
Then visit `http://localhost:5000/` in your browser.

---

## 🛡️ Security & Performance

- **Environment Secrets**: No API keys are exposed in the frontend. All AI logic is proxied through the backend.
- **CSRF Tokens**: All `POST` requests in the frontend automatically fetch and inject a CSRF token from the API.
- **SQLite WAL**: Enabled "Write-Ahead Logging" to prevent database locks during concurrent student/guardian sessions.

---

## 📜 License
Developed as a premium financial literacy platform for teenagers and young adults.

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    age INTEGER NOT NULL,
    skills TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    module_name TEXT NOT NULL,
    status TEXT DEFAULT 'not_started',
    score INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Seed data for modules
-- These will be used by the rule engine to suggest content

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    domain TEXT NOT NULL,
    description TEXT NOT NULL,
    type TEXT NOT NULL,
    eligibility TEXT NOT NULL,
    posted_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    apply_link TEXT
);

CREATE TABLE IF NOT EXISTS gamification (
    user_id INTEGER PRIMARY KEY,
    xp INTEGER DEFAULT 0,
    current_streak INTEGER DEFAULT 0,
    last_active DATE,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

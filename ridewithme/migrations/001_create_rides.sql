CREATE TABLE IF NOT EXISTS rides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL,
    start_datetime TEXT NOT NULL,
    max_participants INTEGER NOT NULL,
    leader_name TEXT NOT NULL,
    leader_contact TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

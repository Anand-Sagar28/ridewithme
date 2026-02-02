CREATE TABLE IF NOT EXISTS ride_participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    ride_id INTEGER NOT NULL,
    joined_at TEXT DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(user_id, ride_id)
);

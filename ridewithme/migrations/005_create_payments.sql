CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    ride_id INTEGER,
    amount INTEGER,
    status TEXT,
    payment_ref TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

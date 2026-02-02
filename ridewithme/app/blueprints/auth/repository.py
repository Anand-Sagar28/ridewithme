from app.db import get_db

def create_user(name, email, password_hash):
    db = get_db()
    db.execute("""
        INSERT INTO users (name, email, password_hash)
        VALUES (?, ?, ?)
    """, (name, email, password_hash))
    db.commit()

def get_user_by_email(email):
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )
    return cursor.fetchone()

def get_user_by_id(user_id):
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )
    return cursor.fetchone()

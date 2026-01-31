from app.db import get_db

def get_upcoming_rides():
    db = get_db()
    cursor = db.execute("""
        SELECT *,
        (max_participants) as available_slots
        FROM rides
        ORDER BY start_datetime ASC
    """)
    return cursor.fetchall()

def create_ride(data):
    db = get_db()
    db.execute("""
        INSERT INTO rides
        (title, description, start_location, end_location,
         start_datetime, max_participants, leader_name, leader_contact)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["title"],
        data.get("description"),
        data["start_location"],
        data["end_location"],
        data["start_datetime"],
        data["max_participants"],
        data["leader_name"],
        data["leader_contact"],
    ))
    db.commit()

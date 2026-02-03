from .repository import get_upcoming_rides, create_ride
from .repository import (
    get_ride_by_id,
    count_participants,
    add_participant,
    has_user_joined,
    update_participation_code,
    create_payment,
    mark_payment_success
)
from .repository import get_participation_code
from app.utils.codes import generate_code
from app.blueprints.auth.repository import get_user_by_id

import secrets


def join_ride(user_id, ride_id):
    ride = get_ride_by_id(ride_id)
    if not ride:
        return False, "Ride not found"

    if has_user_joined(user_id, ride_id):
        return False, "Already joined"

    current = count_participants(ride_id)
    if current >= ride["max_participants"]:
        return False, "Ride full"

    add_participant(user_id, ride_id)
    user = get_user_by_id(user_id)
    code = generate_code(user["name"])
    update_participation_code(user_id, ride_id, code)
    create_payment(user_id, ride_id, 49)

    return True, None


def list_rides():
    return get_upcoming_rides()

def add_ride(data):
    create_ride(data)

def simulate_payment(user_id, ride_id):
    ref = secrets.token_hex(4).upper()
    mark_payment_success(user_id, ride_id, ref)
    return ref

def get_user_code(user_id, ride_id):
    return get_participation_code(user_id, ride_id)



from .repository import get_upcoming_rides, create_ride
from .repository import (
    get_ride_by_id,
    count_participants,
    add_participant,
    has_user_joined
)

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
    return True, None


def list_rides():
    return get_upcoming_rides()

def add_ride(data):
    create_ride(data)

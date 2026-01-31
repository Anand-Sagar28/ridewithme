from .repository import get_upcoming_rides, create_ride

def list_rides():
    return get_upcoming_rides()

def add_ride(data):
    create_ride(data)

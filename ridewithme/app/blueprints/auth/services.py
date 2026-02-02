from werkzeug.security import generate_password_hash, check_password_hash
from .repository import create_user, get_user_by_email

def register_user(name, email, password):
    existing = get_user_by_email(email)
    if existing:
        return False, "Email already exists"

    password_hash = generate_password_hash(password)
    create_user(name, email, password_hash)
    return True, None

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if not user:
        return None

    if check_password_hash(user["password_hash"], password):
        return user

    return None

import secrets

def generate_code(username):
    rand = secrets.token_hex(2).upper()
    return f"{username.upper()}-{rand}"

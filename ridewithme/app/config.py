import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "dev-secret"
    ADMIN_MODE = True
    DATABASE = os.path.join(BASE_DIR, "..", "ridewithme.db")

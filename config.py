import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("YOUR_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

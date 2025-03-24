import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'changeme'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///zentasker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

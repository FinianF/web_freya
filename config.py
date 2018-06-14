import os

class Config():
    DEBUG = True

    CSRF_ENABLED = True

    SECRET_KEY = 'ANGRY_ALPACA_LOL'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
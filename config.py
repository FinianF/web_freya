import os

class Config():
    DEBUG = True

    CSRF_ENABLED = True

    SECRET_KEY = 'ANGRY_ALPACA_LOL'
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///../freya.db"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True

    ASSETS_DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TELEMETRY_UPDATE_PERIOD_MS = 500

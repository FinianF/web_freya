import os

class Config(object):
    DEBUG = True

    CSRF_ENABLED = True

    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'

class ProductionConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
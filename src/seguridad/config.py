from decouple import config

class Config:
    SECRET_KEY = config('KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
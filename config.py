import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '329ijavb93nv0a9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    EVE_SECRET_KEY = 'zX9tLWs2ykSu9VliH6XVp3Gw1VkpGRrJpFJV3wU6'
    EVE_CLIENT_ID = 'e6af6e9d4916455e86d924ed97044895'
    EVE_CALLBACK_URL = 'http://localhost:5000/char/callback'
    EVE_USER_AGENT = 'eCorpManager'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://eCorpMgmt:devel0pment@localhost/eCorpMgmt_DEV'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ""


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
    }

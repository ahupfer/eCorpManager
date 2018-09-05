import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '329ijavb93nv0a9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'

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

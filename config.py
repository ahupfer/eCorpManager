import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or '329ijavb93nv0a9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    EVESSO = dict(
        consumer_key='e6af6e9d4916455e86d924ed97044895',
        consumer_secret='zX9tLWs2ykSu9VliH6XVp3Gw1VkpGRrJpFJV3wU6',
        base_url='https://login.eveonline.com/oauth/',
        access_token_url='/oauth/token',
        access_token_method='POST',
        authorize_url='/oauth/authorize',
        request_token_params={'scope': 'esi-industry.read_character_mining.v1'}
    )

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
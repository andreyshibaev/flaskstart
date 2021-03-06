import os

# from dotenv import load_dotenv
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

class Config(object):
    DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_ECHO = True
    ENV=os.environ.get("FLASK_ENV")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///demo.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@localhost/flaskstart'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/flaskstart'
    SECURITY_PASSWORD_SALT = '$&#)(^?@'
    SECURITY_FLASH_MESSAGES = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_CHECK_BREACHED = 'strict'
    SECURITY_EMAIL_SENDER = 'demo@test.ru'
    SECURITY_CONFIRMABLE = False
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_LOGIN_VIEW = '/profile'
    SECURITY_POST_REGISTER_VIEW = '/profile'
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = True
    FLASK_ADMIN_SWATCH = 'superhero'
    DEBUG_TB_PROFILER_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BABEL_DEFAULT_LOCALE = 'ru'

    # for flask mail
    MAIL_USE_SSL=False
    MAIL_USE_TLS=True
    MAIL_DEBUG = True
    # MAIL_DEFAULT_SENDER = 'demo@test.ru'
    MAIL_SERVER=os.environ.get("MAIL_SERVER")
    MAIL_PORT=os.environ.get("MAIL_PORT")
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")


class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_HOST = os.environ.get('POSTGRES_HOST')
    DB_PORT = os.environ.get('POSTGRES_PORT') or 5432
    DB_NAME = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
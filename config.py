import os

# from dotenv import load_dotenv
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

class Config(object):
    DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///demo.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@localhost/flaskstart'
    SECURITY_PASSWORD_SALT = '$&#)('
    SECURITY_PASSWORD_HASH = 'sha512_crypt'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    ENV=os.environ.get("FLASK_ENV")
    # DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")
from flask import Flask
from sqlalchemy import create_engine
from apps.newapp.views import newapp
from apps.profile.views import profile
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

migrate = Migrate()
db = SQLAlchemy() 

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# for admin
from flask_admin import Admin


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(newapp)
    app.register_blueprint(profile)
    admin = Admin(app, name='My admin')
    return app

# from apps.newapp import models  

if __name__ == "__main__":
    create_app().run()
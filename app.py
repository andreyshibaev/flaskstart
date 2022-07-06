from flask import Flask
from sqlalchemy import create_engine
from apps.homeapp.views import homeapp
from apps.profile.views import profile
from database.database import db
from flask_migrate import Migrate
from config import Config
# from flask_mysqldb import MySQL
from flask_debugtoolbar import DebugToolbarExtension
from flask_security import Security, SQLAlchemyUserDatastore, hash_password, current_user


# for admin
from flask_admin import Admin
from apps.profile.admin import UserView, RoleView
from apps.profile.models import User, Role

from apps.profile import models 

# variables
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
migrate = Migrate()
toolbar = DebugToolbarExtension()


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    migrate.init_app(app, db)
    db.init_app(app)
    app.register_blueprint(homeapp)
    app.register_blueprint(profile)
    admin = Admin(app, name='My admin', template_mode='bootstrap4')
    admin.add_view(UserView(User, db.session))
    admin.add_view(RoleView(Role, db.session))
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # create test admin user

    # @app.before_first_request
    # def create_user():
    #     db.create_all()
    #     if not user_datastore.find_user(email="user@mail.ru"):
    #         user_datastore.create_user(email="user@mail.ru", password=hash_password("rewq4321"))
    #     db.session.commit()

    #update msql
    
    # mysql = MySQL(app)
    # def updatedb():
    #     cur = MySQL.connection.cursor()
    #     cur.execute('')
    #     cur.fetchall()
    #     cur.close()

    #debugtoolbar
    toolbar.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run() 
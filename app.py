from flask import Flask
from sqlalchemy import create_engine
from apps.newapp.views import newapp
from apps.profile.views import profile
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_mysqldb import MySQL

from flask_security import Security, SQLAlchemyUserDatastore


migrate = Migrate()
db = SQLAlchemy()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# for admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from apps.profile.models import User, Role

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    mysql = MySQL(app)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(newapp)
    app.register_blueprint(profile)
    app.config['FLASK_ADMIN_SWATCH'] = 'superhero'
    admin = Admin(app, name='My admin', template_mode='bootstrap4')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    def updatedb():
        cur = MySQL.connection.cursor()
        cur.execute('')
        cur.fetchall()
        cur.close()
    # @app.before_first_request
    # def create_user():
    #     db.create_all()
    #     user_datastore.create_user(email='user@mail.ru', password='000')
    #     db.session.commit()
    return app

from apps.profile import models  

if __name__ == "__main__":
    create_app().run() 
from app import db
from flask_security import RoleMixin, UserMixin
from flask_security.models import fsqla_v2 as fsqla
fsqla.FsModels.set_db_info(db, user_table_name="myuser", role_table_name="myrole")

# class Role(db.Model, fsqla.FsRoleMixin):
#     __tablename__ = "myrole"

# class User(db.Model, fsqla.FsUserMixin):
#     __tablename__ = "myuser"

class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "myrole"

class User(db.Model, UserMixin):
    __tablename__ = "myuser"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

                        


                            
from database.database import db
from flask_security.models import fsqla_v2 as fsqla
fsqla.FsModels.set_db_info(db, user_table_name="myuser", role_table_name="myrole")


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "myrole"

class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = "myuser"                
                            
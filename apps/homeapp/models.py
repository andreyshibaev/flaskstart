from database.database import db                         

class Slider(db.Model):
    __tablename__ = 'slides'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)

    def __repr__(self):
	    return "<{}:{}>".format(self.id,  self.title)
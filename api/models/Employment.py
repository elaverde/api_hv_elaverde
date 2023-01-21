from api.config import db

class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enterprise = db.Column(db.String(256), nullable=False)
    charge = db.Column(db.String(256), nullable=False)
    dateEntry = db.Column(db.Date(), nullable=False)
    dateEnd = db.Column(db.Date(), nullable=True)
    work = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.Text(), nullable=False)
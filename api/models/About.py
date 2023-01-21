from api.config import db

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    lastname = db.Column(db.String(256), nullable=False)
    birthdate = db.Column(db.Date(), nullable=False)
    location = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(256), nullable=False)
    country = db.Column(db.String(256), nullable=False)
    about = db.Column(db.Text(), nullable=False)
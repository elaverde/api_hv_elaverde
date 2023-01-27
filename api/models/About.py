from api.config import db

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    lastname = db.Column(db.String(256), nullable=False)
    birthdate = db.Column(db.Date(), nullable=False)
    civil_status = db.Column(db.String(20), nullable=False)
    dni = db.Column(db.String(15), nullable=False)
    degree = db.Column(db.String(256), nullable=False)
    location = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    site = db.Column(db.Text(), nullable=False)
    city = db.Column(db.String(256), nullable=False)
    country = db.Column(db.String(256), nullable=False)
    about = db.Column(db.Text(), nullable=False)
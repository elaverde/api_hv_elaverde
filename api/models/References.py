from api.config import db

class References(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    title = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Integer(), nullable=False)

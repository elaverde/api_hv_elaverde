from api.config import db

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    percentage = db.Column(db.Integer, nullable=False)
    icon = db.Column(db.String(30), nullable=False)
    url = db.Column(db.Text(), nullable=False)


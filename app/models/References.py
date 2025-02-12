from app import db

class References(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    title = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Integer(), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'phone': self.phone,
            'type': self.type
        }

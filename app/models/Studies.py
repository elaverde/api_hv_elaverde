from app import db

class Studies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    institution = db.Column(db.String(256), nullable=False)
    dateEntry = db.Column(db.Date(), nullable=False)
    dateEnd = db.Column(db.Date(), nullable=True)
    direction = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.String(256), nullable=False)
    important = db.Column(db.Boolean(), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'institution': self.institution,
            'dateEntry': self.dateEntry,
            'dateEnd': self.dateEnd,
            'direction': self.direction,
            'description': self.description,
            'photo': self.photo,
            'important': self.important
        }
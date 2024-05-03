from app import db

class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enterprise = db.Column(db.String(256), nullable=False)
    charge = db.Column(db.String(256), nullable=False)
    dateEntry = db.Column(db.Date(), nullable=False)
    dateEnd = db.Column(db.Date(), nullable=True)
    work = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.Text(), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'enterprise': self.enterprise,
            'charge': self.charge,
            'dateEntry': self.dateEntry.strftime('%Y-%m-%d'),
            'dateEnd': self.dateEnd.strftime('%Y-%m-%d'),
            'work': self.work,
            'photo': self.photo
        }
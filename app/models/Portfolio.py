from app import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    logo = db.Column(db.Text(), nullable=False)
    photo = db.Column(db.Text(), nullable=False)
    link = db.Column(db.Text(), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'logo': self.logo,
            'photo': self.photo,
            'link': self.link
        }
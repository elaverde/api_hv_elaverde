from app import db

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
    linkedin = db.Column(db.String(256), nullable=False)
    github = db.Column(db.String(256), nullable=False)
    gitlab = db.Column(db.String(256), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'birthdate': self.birthdate,
            'civil_status': self.civil_status,
            'dni': self.dni,
            'degree': self.degree,
            'location': self.location,
            'phone': self.phone,
            'address': self.address,
            'email': self.email,
            'site': self.site,
            'city': self.city,
            'country': self.country,
            'about': self.about,
            'linkedin': self.linkedin,
            'github': self.github,
            'gitlab': self.gitlab
        }
from marshmallow import Schema, fields

class AboutSchema(Schema):
    id = fields.Integer(dump_only=True)   
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    birthdate = fields.Date(required=True)
    civil_status = fields.String(required=True)
    dni = fields.String(required=True)
    degree = fields.String(required=True)
    location = fields.String(required=True)
    phone = fields.String(required=True)
    address = fields.String(required=True)
    email = fields.String(required=True)
    site = fields.String(required=True)
    city = fields.String(required=True)
    country = fields.String(required=True)
    about = fields.String(required=True)
    linkedin = fields.String(required=True)
    github = fields.String(required=True)
    gitlab = fields.String(required=True)
    
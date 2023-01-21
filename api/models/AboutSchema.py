from marshmallow import Schema, fields

class AboutSchema(Schema):
    id = fields.Integer(dump_only=True)   
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    birthdate = fields.Date(required=True)
    location = fields.String(required=True)
    email = fields.String(required=True)
    city = fields.String(required=True)
    country = fields.String(required=True)
    about = fields.String(required=True)
    
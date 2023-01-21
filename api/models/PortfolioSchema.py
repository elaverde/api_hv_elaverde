from marshmallow import Schema, fields

class PortfolioSchema(Schema):
    id = fields.Integer(dump_only=True) #id
    title = fields.String(required=True) #title
    subtitle = fields.String(required=True) #subtitle
    description = fields.String(required=True) #description
    logo = fields.String(required=True) #logo
    photo = fields.String(required=True) #photo
    link = fields.String(required=True) #link
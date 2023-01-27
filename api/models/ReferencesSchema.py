from marshmallow import Schema, fields

class ReferencesSchema(Schema):
    id = fields.Integer(dump_only=True) #id
    title = fields.String(required=True) #title
    name = fields.String(required=True) #name
    phone = fields.String(required=True) #phone
    type = fields.Integer(required=True) #type
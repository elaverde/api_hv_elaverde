from marshmallow import Schema, fields

class SkillsSchema(Schema):
    id = fields.Integer(dump_only=True) #id
    name = fields.String(required=True) #name
    percentage = fields.Integer(required=True) #percentage
    icon = fields.String(required=True) #icon
    url = fields.String(required=True) #url

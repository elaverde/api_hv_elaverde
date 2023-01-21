from marshmallow import Schema, fields

class EmploymentSchema(Schema):
    class Meta:
        charset = 'utf-8'
    id = fields.Integer(dump_only=True)                 #id
    enterprise = fields.String(encoding='utf-8')        #empresa
    charge = fields.String(encoding='utf-8')            #cargo
    dateEntry = fields.Date()                           #fecha de ingreso
    dateEnd = fields.Date()                             #fecha de salida
    work = fields.String(encoding='utf-8')              #labor en la empresa
    photo = fields.String(encoding='utf-8')             #foto de la empresa
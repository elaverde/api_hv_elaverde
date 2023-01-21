from marshmallow import Schema, fields

class StudiesSchema(Schema):
    id = fields.Integer(dump_only=True) #id
    title = fields.String()             #titulo del estudio
    institution = fields.String()       #institucion en la que realizo el estudio
    dateEntry = fields.Date()           #fecha de ingreso
    dateEnd = fields.Date()             #fecha de salida
    direction = fields.String()         #direccion de la institucion
    description = fields.String()       #descripcion del estudio
    photo = fields.String()             #foto del estudio
    important = fields.Boolean()        #importancia del estudio

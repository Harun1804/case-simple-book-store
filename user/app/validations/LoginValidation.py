from marshmallow import Schema, fields, validate

class LoginValidation(Schema):
  username = fields.Str(required=True, validate=validate.Length(min=1))
  password = fields.Str(required=True, validate=validate.Length(min=1))
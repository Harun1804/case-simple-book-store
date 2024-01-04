from marshmallow import Schema, fields, validate

class StoreBookValidation(Schema):
  title = fields.Str(required=True, validate=validate.Length(min=1))
  author = fields.Str(required=True, validate=validate.Length(min=1))
  publisher = fields.Str(required=True, validate=validate.Length(min=1))
  year = fields.Int(required=True)
  is_available = fields.Bool(required=True)
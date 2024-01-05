from marshmallow import Schema, fields

class UpdateBookAvailableValidation(Schema):
  is_available = fields.Bool(required=True)
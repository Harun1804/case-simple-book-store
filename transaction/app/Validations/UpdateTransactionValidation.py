from marshmallow import Schema, fields, validate

class UpdateTransactionValidation(Schema):
  status = fields.Str(required=True, validate=validate.Length(min=1), validate=validate.OneOf(["borrowed", "returning"]))
from marshmallow import Schema, fields, validate, validates

class StoreTransactionValidation(Schema):
  user_id = fields.Int(required=True, validate=validate.Range(min=1))
  borrower_date = fields.Date(required=True)
  books = fields.List(fields.Int(), required=True, validate=validate.Length(min=1))

  @validates('borrower_date')
  def validate_date(self, value):
    if value == "":
      raise validate.ValidationError('Date cannot be empty.')

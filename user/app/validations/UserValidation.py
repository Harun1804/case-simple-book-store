from marshmallow import Schema, fields, validate, validates
from app.models.user import User

class UserValidation(Schema):
  id = fields.Int(required=False)
  username = fields.Str(required=True, validate=validate.Length(min=1))
  password = fields.Str(required=False)
  role = fields.Str(required=True, validate=validate.Length(min=1))

  @validates('username')
  def validate_username(self, value):
    user = User.query.filter_by(username=value).first()
    if user and (self.context.get('id') is None or self.context.get('id') != user.id):
      raise validate.ValidationError('Username already exists')

  @validates('password')
  def validate_password(self, value):
      if self.context.get('id') is None and (value is None or len(value) < 1):
        raise validate.ValidationError('Password Required')
from marshmallow import Schema, fields, validate, validates
from app.models.user import User

class UserValidation(Schema):
  id = fields.Int(required=False)
  username = fields.Str(required=True, validate=validate.Length(min=1))
  password = fields.Str(required=False)
  role = fields.Str(required=True, validate=validate.OneOf(["admin", "member"]))

  @validates('username')
  def validate_username(self, value):
    user = User.query.filter_by(username=value).first()
    context_id = int(self.context.get('id')) if self.context.get('id') else None
    if user and (context_id is None or context_id != user.id):
        raise validate.ValidationError('Username already exists')

  @validates('password')
  def validate_password(self, value):
      if self.context.get('id') is None and (value is None or len(value) < 1):
        raise validate.ValidationError('Password Required')
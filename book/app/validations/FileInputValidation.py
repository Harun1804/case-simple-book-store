from marshmallow import fields, ValidationError
from werkzeug.datastructures import FileStorage

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(file: FileStorage):
  return '.' in file.filename and \
    file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class FileField(fields.Field):
  def __deserialize__(self, value, attr, data, **kwargs):
    if value is None:
      return None

    if not isinstance(value, FileStorage):
      raise ValidationError('Invalid input type.')

    if not allowed_file(value):
      raise ValidationError('Invalid file type.')

    return value
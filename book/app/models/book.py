from app import db
from datetime import datetime

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  publisher = db.Column(db.String(100), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  is_available = db.Column(db.Boolean, default=True)
  thumbnail = db.Column(db.String(100), nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

  def __repr__(self):
    return '<Book {}>'.format(self.title)
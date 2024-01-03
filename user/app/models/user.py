from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  role = db.Column(db.String(10), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

  def __repr__(self):
    return '<User {}>'.format(self.username)
  
  def setPassword(self, password):
    self.password = generate_password_hash(password)
  
  def checkPassword(self, password):
    return check_password_hash(self.password, password)
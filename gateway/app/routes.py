from app import app
from flask import request
from app.controllers import BookController
from flask_jwt_extended import jwt_required

@app.route('/admin/books', methods=['GET'])
@jwt_required()
def books():
  return BookController.index()
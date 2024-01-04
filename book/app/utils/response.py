from flask import jsonify, make_response

def success(values = [], message = 'Success', status = 200):
  response = {
    'message': message,
    'result': values
  }
  return make_response(jsonify(response)), status

def error(message = 'Error', status = 400):
  response = {
    'message': message
  }
  return make_response(jsonify(response)), status

def validateError(message = 'validate error', code = 422):
  response = {
    'message': message
  }

  return make_response(jsonify(response)), code
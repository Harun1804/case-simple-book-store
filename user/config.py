import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  HOST = str(os.environ.get('DB_HOST'))
  DBNAME = str(os.environ.get('DB_NAME'))
  USER = str(os.environ.get('DB_USER'))
  PASS = str(os.environ.get('DB_PASS'))

  JWT_SECRET_KEY = str(os.environ.get('JWT_SECRET'))

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USER + ':' + PASS + '@' + HOST + '/' + DBNAME
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True

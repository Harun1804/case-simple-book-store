import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  HOST = str(os.environ.get('DB_HOST'))
  DBNAME = str(os.environ.get('DB_NAME'))
  USER = str(os.environ.get('DB_USER'))
  PASS = str(os.environ.get('DB_PASS'))

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USER + ':' + PASS + '@' + HOST + '/' + DBNAME
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True

  MINIO_ENDPOINT = str(os.environ.get('MINIO_ENDPOINT'))
  MINIO_ACCESS_KEY = str(os.environ.get('MINIO_ACCESS_KEY'))
  MINIO_SECRET_KEY = str(os.environ.get('MINIO_SECRET_KEY'))
  MINIO_SECURE = os.environ.get('MINIO_SECURE') == 'True'
  MINIO_REGION = str(os.environ.get('MINIO_REGION'))

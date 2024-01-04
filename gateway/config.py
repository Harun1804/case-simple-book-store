import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  JWT_SECRET_KEY = str(os.environ.get('JWT_SECRET'))

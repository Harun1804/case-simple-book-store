from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from minio import Minio

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
storage = Minio(
  Config.MINIO_ENDPOINT,
  access_key=Config.MINIO_ACCESS_KEY,
  secret_key=Config.MINIO_SECRET_KEY,
  secure=Config.MINIO_SECURE,
  region=Config.MINIO_REGION
)
cors = CORS(app)

from app.models import book
from app import routes

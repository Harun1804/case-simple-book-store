from config import Config
from flask import Flask
from flask_cors import CORS
from app.routes import BookRoute
from app.docs import document
from app.utils import extension

app = Flask(__name__)
app.config.from_object(Config)
extension.jwt.init_app(app)

app.register_blueprint(BookRoute.blueprint)
app.register_blueprint(document)
cors = CORS(app)

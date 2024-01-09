from config import Config
from flask import Flask
from flask_cors import CORS
from app.routes import AuthRoute, BookRoute, UserRoute, TransactionRoute
from app.docs import document
from app.utils import extension, helper

app = Flask(__name__)
app.secret_key = helper.appSecretKey()
app.config.from_object(Config)
extension.jwt.init_app(app)
@app.route('/')
def index():
  return 'Harun Tampan'

app.register_blueprint(AuthRoute.blueprint)
app.register_blueprint(BookRoute.blueprint)
app.register_blueprint(UserRoute.blueprint)
app.register_blueprint(TransactionRoute.blueprint)
app.register_blueprint(document)
cors = CORS(app)

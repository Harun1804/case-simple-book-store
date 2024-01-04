from config import Config
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Bookstore Microservice"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
cors = CORS(app)

from app import routes

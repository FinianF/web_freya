from flask import Flask, Blueprint
from flask_assets import Environment
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy

app = Flask(
__name__,
static_folder="static",
template_folder="templates"
)

from config import *
app.config.from_object(DevelopmentConfig())

jsonrpc = JSONRPC(service_url='/api')
db = SQLAlchemy()


assets = Environment(app)
import freya.assets

map_bp = Blueprint('map', __name__, url_prefix="/map")

import freya.blueprints.map
import freya.blueprints.rpc

app.register_blueprint(map_bp)
jsonrpc.init_app(app)

db.init_app(app)

import freya.models


if __name__ == '__main__':
    app.run()

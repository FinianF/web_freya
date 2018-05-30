from flask import Flask, Blueprint
from flask_assets import Environment

app = Flask(
__name__,
static_folder="static",
template_folder="templates"
)

assets = Environment(app)
import freya.assets

map_bp = Blueprint('map', __name__, url_prefix="/map")
import freya.blueprints.map
app.register_blueprint(map_bp)

from config import *
app.config.from_object(DevelopmentConfig())

if __name__ == '__main__':
    app.run()

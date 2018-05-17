from flask import Flask
import os

from freya.assets import assets
from freya.blueprints.map import map


app = Flask(
__name__,
static_folder="static",
template_folder="templates"
)
app.config.from_object(os.environ['APP_SETTINGS'])

assets.init_app(app)
app.register_blueprint(map)

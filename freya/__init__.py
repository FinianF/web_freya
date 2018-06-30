from flask import Flask, Blueprint
from flask_assets import Environment
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


from config import *

app.config.from_object(DevelopmentConfig())


assets = Environment(app)
jsonrpc = JSONRPC(app, '/api')
db = SQLAlchemy(app)

import freya.assets
import freya.models


mp_bp = Blueprint('main_page', __name__, url_prefix="/")
ft_bp = Blueprint('freya_team', __name__, url_prefix="/freya_team")
map_bp = Blueprint('map', __name__, url_prefix="/map")

import freya.blueprints.page_render
import freya.blueprints.map
import freya.blueprints.rpc

app.register_blueprint(mp_bp)
app.register_blueprint(ft_bp)
app.register_blueprint(map_bp)


if __name__ == '__main__':
    app.run()

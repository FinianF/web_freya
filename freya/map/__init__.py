from flask import Blueprint

bp = Blueprint('map', __name__, url_prefix="/map")

import freya.map.views

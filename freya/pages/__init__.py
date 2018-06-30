from flask import Blueprint

bp = Blueprint('pages', __name__, url_prefix="/")

import freya.pages.views

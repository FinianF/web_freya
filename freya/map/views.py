from flask import render_template
from jinja2 import TemplateNotFound

from freya.map import bp

@bp.route('/')
def map_index():
    try:
        return render_template('map.html')
    except TemplateNotFound:
        abort(404)

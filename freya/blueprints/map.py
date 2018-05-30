from flask import render_template, abort
from jinja2 import TemplateNotFound

from freya import map_bp

@map_bp.route('/')
def map_index():
    try:
        return render_template('map.html')
    except TemplateNotFound:
        abort(404)
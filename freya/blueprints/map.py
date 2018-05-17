from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

map = Blueprint('map',__name__,url_prefix="/map")

@map.route('/')
def map_index():
    try:
        return render_template('map.html')
    except TemplateNotFound:
        abort(404)
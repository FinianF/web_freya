from flask import render_template, abort
from jinja2 import TemplateNotFound

from freya import mp_bp
from freya import ft_bp
from freya import map_bp

@map_bp.route('/')
def map_index():
    try:
        return render_template('map.html')
    except TemplateNotFound:
        abort(404)

@mp_bp.route('/')
def mp_bp_index():
    try:
        return render_template('main_page.html')
    except TemplateNotFound:
        abort(404)

@ft_bp.route('/')
def ft_bp_index():
    try:
        return render_template('freya_team.html')
    except TemplateNotFound:
        abort(404)
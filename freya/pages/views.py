from freya.pages import bp

@bp.route('/')
def mp_bp_index():
    try:
        return render_template('main_page.html')
    except TemplateNotFound:
        abort(404)

@bp.route('/freya_team')
def ft_bp_index():
    try:
        return render_template('freya_team.html')
    except TemplateNotFound:
        abort(404)

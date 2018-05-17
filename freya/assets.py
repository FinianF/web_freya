from flask_assets import Environment, Bundle


page_css = Bundle("scss/page.css")
op_css = Bundle("OpenLayers/ol.css")
op_js = Bundle("OpenLayers/ol.js")

assets = Environment()
assets.register("page_css", page_css)
assets.register("op_css", op_css)
assets.register("op_js", op_js)


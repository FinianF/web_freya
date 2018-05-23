from flask_assets import Environment, Bundle


page_css = Bundle("scss/page.css")
op_css = Bundle("OpenLayers/ol.css")
op_js = Bundle("OpenLayers/ol.js")
map_js = Bundle("js/map.js")

assets = Environment()
assets.register("page_css", page_css)
assets.register("op_css", op_css)
assets.register("op_js", op_js)
assets.register("map_js", map_js)


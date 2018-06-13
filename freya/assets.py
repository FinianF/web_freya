from flask_assets import Bundle
from freya import assets

page_css = Bundle("css/page.css")
map_css = Bundle("OpenLayers/ol.css", "Bootstrap/bootstrap.css", "css/map.css",  filters="cssmin")
bt_js = Bundle( "Bootstrap/jquery-3.3.1.js", "Bootstrap/popper.js", "Bootstrap/tooltip.min.js", "Bootstrap/bootstrap.js", filters="jsmin")
map_js = Bundle( bt_js, "OpenLayers/ol.js", "js/map.js",  filters="jsmin")

assets.register("page_css", page_css)
assets.register("map_css", map_css)
assets.register("map_js", map_js)



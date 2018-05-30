from flask_assets import Bundle
from freya import assets

page_css = Bundle("css/page.css")
map_css = Bundle("OpenLayers/ol.css", "css/map.css", "css/bootstrap.css", filters="cssmin")
map_js = Bundle("OpenLayers/ol.js", "js/map.js", "js/bootstrap.js", "js/jquery-3.3.1.js", filters="jsmin")

assets.register("page_css", page_css)
assets.register("map_css", map_css)
assets.register("map_js", map_js)



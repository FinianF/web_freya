from flask_assets import Bundle
from freya import assets

page_css = Bundle("css/page.css", "css/freya_team.css")
ft_css = Bundle("css/freya_team.css")
map_css = Bundle("OpenLayers/ol.css", "css/map.css", filters="cssmin")
bt_css = Bundle("Bootstrap/bootstrap.css", filters="cssmin")
bt_js = Bundle( "Bootstrap/jquery-3.3.1.js", "Bootstrap/popper.js", "Bootstrap/bootstrap.js", filters="jsmin")
map_js = Bundle("OpenLayers/ol.js", "js/map.js", filters="jsmin")
cat_pic = Bundle("pic/kitty.jpg")

assets.register("bt_css", bt_css)
assets.register("ft_css", ft_css)
assets.register("page_css", page_css)
assets.register("map_css", map_css)
assets.register("bt_js", bt_js)
assets.register("map_js", map_js)
assets.register("cat_pic", cat_pic)



from flask import Flask

import logging

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

from config import *
app.config.from_object(DevelopmentConfig())

from freya.database import db
db.init_app(app)

from freya.api import rpc
rpc.init_app(app)

from freya.assets import assets
assets.init_app(app)

from freya.pages import bp as pages_bp
from freya.map import bp as map_bp
app.register_blueprint(pages_bp)
app.register_blueprint(map_bp)


if __name__ == '__main__':
    app.run()

import os
from flask_script import Manager

from freya.manage import app

#app.config.from_object(os.environ['APP_SETTINGS'])
#manager = Manager(app)

if __name__ == '__main__':
    app.run(debug=True)

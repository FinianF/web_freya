import os
from flask import Flask

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)

if __name__ == "__main__":
    app.run(debug=True)
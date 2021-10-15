from flask import Flask
from extension import conf

def create_app():
    app = Flask(__name__)
    conf.init_app(app)
    conf.load_libs(app)
    return app



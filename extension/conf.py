from importlib import import_module
from dynaconf import FlaskDynaconf

def load_libs(app):
    for lib in app.config.get("EXTENSIONS"):
        modulo = import_module(lib)
        modulo.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
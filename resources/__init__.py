from flask_restful import Api
from flask import Blueprint

from .temp_resource import Temp_resource, Temp_resource_get_all
from .lux_resource import Lux_resource_get_all, Lux_resource

bp = Blueprint("my_api", __name__, url_prefix='/api_V1')
api = Api(bp)
api.add_resource(Temp_resource, '/temp/<data>')
api.add_resource(Temp_resource_get_all,'/temp/get_all/')
api.add_resource(Lux_resource, '/lux/<data>')
api.add_resource(Lux_resource_get_all, '/lux/get_all/')

def init_app(app):
    app.register_blueprint(bp)
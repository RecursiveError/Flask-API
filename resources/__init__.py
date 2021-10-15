from flask_restful import Api
from flask import Blueprint

from .temp_resource import Temp_resource
#from .luminosidade import
#  
bp = Blueprint("my_api", __name__, url_prefix='/api')
api = Api(bp)
api.add_resource(Temp_resource, '/temp/')

def init_app(app):
    app.register_blueprint(bp)
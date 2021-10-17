from flask import jsonify, request, abort
from flask_restful import Resource
from models.temperatura import Temperatura
from extension.database import db

from datetime import datetime


class Temp_resource_get_all(Resource):
    def get(self):
        temperatura = Temperatura.query.order_by(Temperatura.data).all() or abort(404)
        return jsonify({'temp' :[temp.to_dict() for temp in temperatura]})

class Temp_resource(Resource):
    def get(self, data):
        try: 
            datestr = str(datetime.strptime(data, '%Y-%d-%m'))
            temperatura = Temperatura.query.filter_by(data=data).all() or abort(404)
        except ValueError:
            abort(400, "data invalida")

        return jsonify({'temp' :[temp.to_dict() for temp in temperatura]})

    def post(self, data=None):
        try:
            content = request.get_json() or abort(400)
            temp = Temperatura(content['temp'], content['date'], content['hour'])
            db.session.add(temp)
            db.session.commit()
        except KeyError:
            abort(400, "Json invalido")
        return {'status': 'ok'}


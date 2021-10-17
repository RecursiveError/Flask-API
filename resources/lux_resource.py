from flask import jsonify, request, abort
from flask_restful import Resource
from models.luminosidade import Luminosidade
from extension.database import db

from datetime import datetime


class Lux_resource_get_all(Resource):
    def get(self):
        luminosidade = Luminosidade.query.order_by(Luminosidade.data).all() or abort(404)
        return jsonify({'lux' :[lux.to_dict() for lux in luminosidade]})

class Lux_resource(Resource):
    def get(self, data):
        try: 
            datestr = str(datetime.strptime(data, '%Y-%d-%m'))
            luminosidade = Luminosidade.query.filter_by(data=data).all() or abort(404)
        except ValueError:
            abort(400, "data invalida")
        return jsonify({'lux' :[lux.to_dict() for lux in luminosidade]})

    def post(self, data=None):
        try:
            content = request.get_json() or abort(400)
            lux = luminosidade(content['lux'], content['date'], content['hour'])
            db.session.add(lux)
            db.session.commit()
        except KeyError:
            abort(400, "Json invalido")
        return {'status': 'ok'}


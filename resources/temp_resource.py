from flask_restful import Resource
#from models import temperatura


class Temp_resource(Resource):
    def get(self, data=123):
        return "hello {}".format(data)
    def post(self):
        return "hello world"
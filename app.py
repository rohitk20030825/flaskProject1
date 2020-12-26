from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

names = {"Tim":{"Age":19,"gender":"Male"},
         "Mark":{"Age":21,"gender":"Male"},
         "Tina":{"Age":19,"gender":"Female"}}


class HelloWorld(Resource):
    def get(self,name):
        return names[name]
    def post(self,name):
        return names[name]

api.add_resource(HelloWorld,"/helloworld/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
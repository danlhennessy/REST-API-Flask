from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return{"about" : "Hello World!"}
    def post(self):
        some_json = request.get_json()
        return {'you provided' : some_json}, 201
    
api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True)
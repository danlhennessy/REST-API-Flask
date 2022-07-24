from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creates an id column in the database, primary_key=True means each id will be unique
    name = db.Column(db.String(100), nullable=False) # String limit = 100, nullable=False means it has to have a value
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

#db.create_all() # Initialises database with fields above included, only initialise at the start or it will overrite the data

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video missing", required=True)
video_put_args.add_argument("views", type=int, help="Views of video missing", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on video missing", required=True)

''' Abort No Longer needed since DB inclusion
def abortvid(video_id):
    if video_id not in videos:
        abort(404, message="Video does not exist..")

def abortexisting(video_id):
    if video_id in videos:
        abort(409, message="Vid already exists with that ID..")
'''
class Video(Resource):
    def get(self, video_id):
        abortvid(video_id)
        return videos[video_id]
    def put(self, video_id):
        abortexisting(video_id)
        args = video_put_args.parse_args() #Brings in args from video_put_args defined above
        videos[video_id] = args
        return videos[video_id], 201
    def delete(self, video_id):
        abortvid(video_id)
        del videos[video_id]
        return "", 204
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
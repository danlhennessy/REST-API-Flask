from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video missing", required=True)
video_put_args.add_argument("views", type=int, help="Views of video missing", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on video missing", required=True)

videos = {}

def abortvid(video_id):
    if video_id not in videos:
        abort(404, message="Video does not exist..")

class Video(Resource):
    def get(self, video_id):
        abortvid(video_id)
        return videos[video_id]
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
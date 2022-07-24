from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
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

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of video missing")
video_update_args.add_argument("views", type=int, help="Views of video missing")
video_update_args.add_argument("likes", type=int, help="Likes on video missing")

''' Abort Funcs No Longer needed since DB inclusion
def abortvid(video_id):
    if video_id not in videos:
        abort(404, message="Video does not exist..")

def abortexisting(video_id):
    if video_id in videos:
        abort(409, message="Vid already exists with that ID..")
'''

resource_fields = {'id' : fields.Integer, 'name' : fields.String, 'views' : fields.Integer, 'likes' : fields.Integer}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find this Video ID")
        return result
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exists")
        video = VideoModel(id=video_id, name = args['name'], views = args['views'], likes = args['likes']) # Creates object of class VideoModel using provided args + video_id
        db.session.add(video) # Adds object to DB session
        db.session.commit() # Commits session to DB
        return video, 201
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Video does not exist')
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        db.session.commit()
        return result
    @marshal_with(resource_fields)
    def delete(self, video_id):
        q = input(f"Are you sure you want to delete Video: {video_id}? Y/N")
        if q.lower() == 'y':
            VideoModel.query.filter_by(id=video_id).delete()
            db.session.commit()
        else:
            print(f"Video {video_id} not deleted")
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
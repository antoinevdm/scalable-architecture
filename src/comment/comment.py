from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlite3
import jwt
import json

app = Flask(__name__)
api = Api(app)

class Comments(Resource):
    def get(self):
        query = conn.execute("SELECT * FROM COMMENT") # This line performs query and returns json result
        i=0
        for row in query:
            i = i+1
        return {'Number of comment': i} # Fetches first column that is Employee ID

    def post(self):
        postId = request.form["postId"]
        # postId = request.args.get("postId")
        query = conn.execute("Select USER, VALUE FROM COMMENT WHERE POSTID = "+postId+"");
        result = query.fetchall()
        return result

class Comment(Resource):
    def post(self):
        token = request.form['jwt']
        user= jwt.decode(token, 'scalable')['name']
        postId = request.form['PostId']
        value = request.form['Value']
        query = conn.execute("INSERT INTO COMMENT(USER, POSTID, VALUE) VALUES ('"+user+"', '"+postId+"', '"+value+"')");
        conn.commit()
        return {'status': 'success'}

api.add_resource(Comments, '/comments')
api.add_resource(Comment, '/comment')

if __name__ == '__main__':
    conn = sqlite3.connect('comment.db')
    app.run(port=5001)

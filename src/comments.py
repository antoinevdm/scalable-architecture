from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlite3
import jwt

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        query = conn.execute("SELECT * FROM USERS") # This line performs query and returns json result
        i=0
        for row in query:
            i = i+1
        return {'Number of users': i} # Fetches first column that is Employee ID

    #sql injection : { "Name": "antoine", "Password": "test+\"'); DROP TABLE USERS;"}
    # plus change execute to execute scritpt
    def post(self):
        print(request.json)
        Name = request.json['Name']
        Password = request.json['Password']
        query = conn.execute("INSERT INTO USERS(NAME, PASSWORD) VALUES ('"+Name+"', '"+Password+"')");
        conn.commit()
        return {'status': 'success'}

class User(Resource):
    def post(self):
        print(request.json)
        name = request.json['Name']
        password = request.json['Password']
        query = conn.execute("SELECT PASSWORD FROM USERS WHERE NAME = '"+name+"'");
        realPassword = ""
        for row in query:
            realPassword= row[0]
            print(realPassword)
            break
        if realPassword is "":
            # retrun httpcode
            return 'user does not exist', 404
        if realPassword != password:
            return 'Wrong password', 403

        encoded = jwt.encode({'name': ''+name+''}, 'scalable', algorithm='HS256')
        encoded = encoded.decode('UTF-8')
        return {'token': ''+encoded+''}

api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    conn = sqlite3.connect('comments.db')
    conn.execute('''CREATE TABLE COMMENTS
         (ID INT PRIMARY KEY    AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         POSTID         INT     NOT NULL,
         CONTENT        CHAR(50));''')
    app.run(port=5003)

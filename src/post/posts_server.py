import os
import time
from flask import Flask, request, render_template,redirect, flash, url_for
import json
import datetime 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from posts_db import *
import sys
import jwt

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

token =''

@app.route('/',methods=['POST','GET'])#---------------------------------------------
def show_posts():
    posts= session.query(Post.post_id, Post.user_name, Post.content, Post.time).order_by(Post.post_id.desc()).all()
    return render_template('posts.html', posts = posts, token='')


@app.route('/test/<name>',methods=['POST','GET'])#---------------------------------------------
def show_post_token(name):
    global token
    expected_name = jwt.decode(token,'scalable')['name']
    if(name != expected_name):
        flash("User refused","alert alert-danger")
        return redirect('/')
    posts= session.query(Post.post_id,Post.user_name, Post.content, Post.time).order_by(Post.post_id.desc()).all()
    return render_template('posts.html', posts = posts, token=token, name= expected_name)


@app.route('/api/add_post',methods=['POST','GET'])#---------------------------------------------
def add_post():
    global token
    content = request.form['post']
    token = request.form['jwt']
    name = jwt.decode(token,'scalable')['name']
    session.add(Post(name,content, datetime.datetime.now()))
    session.commit()
    return redirect('/test/'+name)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0')





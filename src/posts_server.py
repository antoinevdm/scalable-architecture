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

@app.route('/',methods=['POST','GET'])#---------------------------------------------
def show_posts():
    posts= session.query(Post.user_name, Post.content, Post.time).order_by(Post.id.desc()).all()
    return render_template('posts.html', posts = posts, token='')

@app.route('/show_posts_token',methods=['POST','GET'])#---------------------------------------------
def show_post_token():
    token=request.args['token']
    posts= session.query(Post.user_name, Post.content, Post.time).order_by(Post.id.desc()).all()
    token = jwt.decode(token,'scalable')
    name = token['name']
    return render_template('posts.html', posts = posts, name=name)


@app.route('/api/add_post',methods=['POST','GET'])#---------------------------------------------
def add_post():
    content = request.form['post']
    token = request.form['jwt']
    name = jwt.decode(token,'scalable')['name']
    session.add(Post(name,content, datetime.datetime.now()))
    session.commit()
    return redirect(url_for('show_post_token', token=token))

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0')





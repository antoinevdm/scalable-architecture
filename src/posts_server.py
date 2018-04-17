import os
import time
from flask import Flask, request, render_template,redirect, flash
import json
import datetime 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from posts_db import *
import sys

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route('/show_posts',methods=['POST','GET'])#---------------------------------------------
def show_posts():
    posts= session.query(Post.user_name, Post.description, Post.time).order_by(Post.id.desc()).all()
    return render_template('posts.html', posts = posts)

@app.route('/api/add_post',methods=['POST','GET'])#---------------------------------------------
def add_post():
    description = request.form['post']
    session.add(Post(None,description, datetime.datetime.now()))
    session.commit()
    return redirect("/show_posts")

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0')




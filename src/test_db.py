import os
import time
import json
import datetime 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from posts_db import *


# create a Session
Session = sessionmaker(bind=engine)
session = Session()


posts= session.query(Post.user_id, Post.description, Post.time).all()
print(posts[0])
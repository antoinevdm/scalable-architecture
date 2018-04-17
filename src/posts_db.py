from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///Twitter.db', echo=False)
Base = declarative_base()
 
########################################################################
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_name = Column(Integer)
    description = Column(String(64))
    time = Column(DateTime)
    #----------------------------------------------------------------------
    def __init__(self,user_id, description, time):
        self.user_id = user_id
        self.description = description  
        self.time = time
# create tables
Base.metadata.create_all(engine)

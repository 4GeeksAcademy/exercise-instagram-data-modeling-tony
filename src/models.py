import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), unique=False, nullable=False)
    last_name = Column(String(250), unique=False, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=False, nullable=False)
    subscription_date = Column(String(250), unique=False, nullable=False)
    guardado = relationship("guardado")
    post = relationship("post")
    estado = relationship("estado")

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "last_name" : self.last_name,
            "email" : self.email,
            "password" : self.password,
            "subscription_date" : self.subscription_date
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, unique=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    post_type = Column(String(250), unique=False, nullable=False)
    posted_date = Column(String(250), unique=False, nullable=False)
    likes = Column(Integer, unique=False, nullable=False)
    shares = Column(Integer, unique=False, nullable=False)
    comments = Column(Integer, unique=False, nullable=False)
    guardado = relationship("guardado")

    def to_dict(self):
        return {
            "id" : self.id,
            "user_name" : self.user_name,
            "post_type" : self.post_type,
            "posted_date" : self.posted_date,
            "likes" : self.likes,
            "shares" : self.shares,
            "comments" : self.comments
        }

class Estado(Base):
    __tablename__ = 'estado'
    id = Column(Integer, unique=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    posted_date = Column(String(250), unique=False, nullable=False)
    views = Column(Integer, unique=False, nullable=False)
    likes = Column(Integer, unique=False, nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "user_name" : self.user_name,  
            "posted_date" : self.posted_date,
            "views" : self.views,
            "likes" : self.likes      
        }

class Guardado(Base):
    __tablename__ = 'guardado'
    id = Column(Integer, unique=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    id_post = Column(Integer, ForeignKey("post.id"))

    def to_dict(self):
        return {
            "id_post" : self.id_post,
            "id_estado" : self.id_estado 
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

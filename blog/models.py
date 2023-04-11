from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from blog.app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'  # optional
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    birth_year = db.Column(db.Integer)

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, username, first_name, last_name, email, birth_year, password):
        self.username = username
        self.first_name =first_name
        self.last_name = last_name
        self.email = email
        self.birth_year = birth_year
        self.password = password


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='author')
    articles = db.relationship("Article", back_populates="author")          # creates list author.article


class Article(db.Model):
    __tablename__ = 'articles'  # optional
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    author = db.relationship('Author', back_populates="articles")           # creates list article.user





from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from http import HTTPStatus
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = "1851339de0a3dc2da7fdefe7a2ff6caaed504caf767073cb3588c32bd38a6565"
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coding_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    post = relationship("Post", back_populates="user")
    comment = relationship("Comment", back_populates="user")

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship("User", back_populates="post")
    comment = relationship("Comment", back_populates="post")

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user = relationship("User", back_populates="comment")
    post = relationship("Post", back_populates="comment")

db.create_all()




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=["POST", "GET"])
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route('/post', methods=["POST", "GET"])
@login_required
def post():
    return render_template("create-post.html")


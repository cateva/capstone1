from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db = SQLAlchemy()#****
bcrypt = Bcrypt()#work with routes in routes.py

def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
    # db.drop_all()
    # db.create_all()

class User(db.Model, UserMixin): #create column of User Model

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) #must be unique , nullable=False can not be blank
    email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') 
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) #one user can have many posts
                                    #use backref = author to locate author, lazy=True:  Typically when you query the database, the data get loaded at once; however, lazy parameter allows you to alternate the way they get loaded. 

    def __repr__(self): #how are object printed when we print out
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(1000), nullable=False) #change to text later
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #link to class User -> id

    def __repr__(self): #how are object printed when we print out
        return f"Post('{self.title}','{self.date_posted}')"
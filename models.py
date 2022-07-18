from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer   
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


from flask_login import login_manager, UserMixin, LoginManager

from flask import Flask
app = Flask(__name__)
login_manager = LoginManager(app)
app = Flask(__name__)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

bcrypt = Bcrypt()#work with routes in routes.py
db = SQLAlchemy()#****

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

    def get_reset_token(self, expires_sec=1800): # userid expired in 1800 secs
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')  

    @staticmethod
    def verify_reset_token(token): 
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

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





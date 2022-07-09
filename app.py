from flask import Flask,render_template, url_for, flash, redirect
import email
from forms import RegistrationForm, LoginForm
from models import User, Post,connect_db
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone1'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

connect_db(app)
db = SQLAlchemy()#****


if __name__ == '__main__':
    app.run(debug=True)

# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]


# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)#generate output from a template file based on the Jinja2 engine that is found in the application's templates folder.


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


# @app.route("/register", methods=['GET', 'POST'])#accept get request, and post the data
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():#check if a form is validate when submitted
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         #get a value of password code, hashed, decode('utf-8')function to make it a string
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user) 
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')#flash in flask to send one time alert msg, also allow another argutment as catogary - 'success'
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)



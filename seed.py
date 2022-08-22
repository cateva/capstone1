from csv import DictReader
from app import db
from models import User, Post


db.drop_all()
db.create_all()


with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/posts.csv') as messages:
    db.session.bulk_insert_mappings(Post, DictReader(posts))


db.session.commit()


# DROP DATABASE IF EXISTS capstone1;

# CREATE DATABASE capstone1;

# \c capstone1

# CREATE TABLE users(
#     id serial PRIMARY KEY,
#     username VARCHAR (50) UNIQUE NOT NULL,
#     password VARCHAR (50) NOT NULL,
#     email VARCHAR (50) UNIQUE NOT NULL,
#     create_on TIMESTAMP NOT NULL,
#     FOREIGN KEY (post_id)
#         REFERENCES POSTS (id),
# );

# CREATE TABLE POSTS(
#     id serial PRIMARY KEY,
#     post TEXT NOT NULL,
#     FOREIGN KEY (post_id)
#         REFERENCES POSTS (id),
# );


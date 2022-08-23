# from csv import DictReader
from app import db
# from models import User, Post


db.drop_all()
db.create_all()


# with open('generator/users.csv') as users:
#     db.session.bulk_insert_mappings(User, DictReader(users))

# with open('generator/posts.csv') as messages:
#     db.session.bulk_insert_mappings(Post, DictReader(posts))


db.session.commit()



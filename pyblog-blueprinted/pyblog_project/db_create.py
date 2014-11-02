__author__ = 'admin'
from project import db
from project.models import Post, User
from datetime import date

db.create_all()

db.session.add(Post('First post', 'this is my first post','Welcome', date(2014, 10, 03), None, 1, 'Mike'))
user = User(user_id='admin', authenticated=False)
user.hash_password('password')
db.session.add(user)

db.session.commit()
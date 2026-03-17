from flask_sqlalchemy import SQLAlchemy
#using SQLAlchemy to connect to database and create tables
db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    #primary key is used to give each user a unique id (consecutive numbers)
    '''string(100) means max len(username) is 100 chars,
    but since we set max len(username) to (3-20) in forms.py so will limit 20 in database as well
    and nullable=false means the field cannot be empty (same as  data_required)
    '''
    username = db.Column(db.String(20), nullable=False)

    email = db.Column(db.String(120), nullable=False)

    password = db.Column(db.String(50), nullable=False)
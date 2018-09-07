from flask_sqlalchemy import SQLAlchemy
from src import db
import hashlib
import time


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


def validate_user(email, password):
    try:
        user = db.session.query(User).filter_by(
            email=email, password=password).one()
        return user
    except:
        return False


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User',
                           backref=db.backref('todos', lazy=True))


class AuthToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User',
                           backref=db.backref('authtoken', lazy=True))

    def __init__(self, **kwargs):
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        token = hash.hexdigest()[:10]
        super(AuthToken, self).__init__(token=token, **kwargs)

def validate_token(email, token):
    try:
        user = db.session.query(AuthToken).filter_by(token=token).join(AuthToken.user, aliased=True).filter_by(email=email).one()
        return user
    except:
        return False
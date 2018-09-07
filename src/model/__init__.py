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

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'summary': self.summary,
            'status':    self.status
        }

    def merge_update(self, data):
        """Merge in data to update attributes in this object"""
        flag = True
        for key, value in data.items():
            if key in ['summary', 'description', 'status']:
                setattr(self, key, value)
            else:
                flag = False

        return flag


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

    def token_is_valid(token):
        """ This needs to be done properly, with a proper token. """
        try:
            print(token)
            print(str(db.session.query(AuthToken).filter_by(token=token)))
            return db.session.query(AuthToken).filter_by(token=token).one()
        except:
            return False


def validate_token(email, token):
    try:
        user = db.session.query(AuthToken).filter_by(token=token).join(
            AuthToken.user, aliased=True).filter_by(email=email).one()
        return user
    except:
        return False

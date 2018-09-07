import pytest
import sys
import os
import json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from flask_sqlalchemy import SQLAlchemy

from src import create_app, db as _db

@pytest.fixture(scope='session')
def test_client():
    flask_app = create_app('flask_test.cfg')
    from src.model import User, Todo, AuthToken
    #db.create_all(app=flask_app)
    #setup_db()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

@pytest.yield_fixture(scope='session')
def db(test_client):
    _db.app = test_client
    _db.drop_all()
    _db.create_all()

    setup_db()

    yield _db

    _db.drop_all()

@pytest.fixture(scope='function', autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()

def setup_db():
    from src.model import User, Todo, AuthToken
    _db.session.add_all([
        User(email="test.user@example.net", password="ValidPassword"),
        User(email="test.user2@example.net", password="ValidPassword2")
    ])
    _db.session.commit()
    token1 = AuthToken(user_id=1)
    token1.token = 'ValidToken'
    _db.session.add_all([
        token1
    ])
    _db.session.commit()

import pytest
import sys
import os
import json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from flask_sqlalchemy import SQLAlchemy

from src import create_app, db

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')
    from src.model import User, Todo, AuthToken
    db.create_all(app=flask_app)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

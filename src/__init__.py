from flask import Flask, abort, request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    db.init_app(app)
    from src.auth import bp as bp_auth
    from src.todo import bp as bp_todo
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_todo)
    return app

def check_token(func):
    """ Wrapper to check token for api endpoints """
    @wraps(func)
    def wrap(*args, **kwargs):
        if not 'auth-token' in request.headers:
            abort(401)
        from src.model import AuthToken
        token = AuthToken.token_is_valid(request.headers['auth-token'])
        print(token)
        if token is not False:
            return func(token=token, *args, **kwargs)
        else:
            return ('', 401)
    return wrap

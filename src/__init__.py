from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

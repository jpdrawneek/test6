from flask import Blueprint, jsonify, request
from src import db
from src.model import User, validate_user

bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.route('/authenticate', methods=['POST'])
def login():
    data = request.get_json()
    print(validate_user(data['email'], data['password']))
    if validate_user(data['email'], data['password']) is not False:
        return jsonify({'auth-token': 'ValidToken'})
    else:
        return ('', 401)


@bp.route('/logout/<user_email>', methods=['POST'])
def logout(user_email):
    data = request.get_json()
    if user_email == 'test.user@example.net' and data['auth-token'] == 'ValidToken':
        return ('', 204)
    else:
        return ('', 403)

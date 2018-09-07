from flask import Blueprint, jsonify, request
from src import db
from src.model import User, validate_user, AuthToken, validate_token

bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.route('/authenticate', methods=['POST'])
def login():
    data = request.get_json()
    user = validate_user(data['email'], data['password'])
    if user is not False:
        token = AuthToken(user_id=user.id)
        db.session.add(token)
        db.session.commit()
        print(token)
        return jsonify({'auth-token': token.token})
    else:
        return ('', 401)


@bp.route('/logout/<user_email>', methods=['POST'])
def logout(user_email):
    data = request.get_json()
    token = validate_token(email=user_email, token=data['auth-token'])
    if token is not False:
        db.session.delete(token)
        db.session.commit()
        return ('', 204)
    else:
        return ('', 403)

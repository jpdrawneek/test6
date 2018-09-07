from flask import Blueprint, jsonify, request

bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.route('/authenticate', methods=['POST'])
def login():
    data = request.get_json()
    if data['email'] == 'test.user@example.net' and data['password'] == 'ValidPassword':
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

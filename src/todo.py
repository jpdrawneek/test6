from flask import Blueprint, jsonify, request

bp = Blueprint('todo', __name__, url_prefix='/api')


@bp.route('/todo', methods=['POST'])
def create():
    return jsonify({'id': 1})


@bp.route('/todo/<todo_id>', methods=['GET'])
def get(todo_id):
    return jsonify({'id': 1})


@bp.route('/todo', methods=['GET'])
def list_all():
    return jsonify([{'id': 1}])


@bp.route('/todo/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    return ('', 204)


@bp.route('/todo/<todo_id>', methods=['PATCH'])
def update_status(todo_id):
    return ('', 204)

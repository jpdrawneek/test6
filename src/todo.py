from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src import db, check_token
from src.model import User, Todo, AuthToken

bp = Blueprint('todo', __name__, url_prefix='/api')

@bp.route('/todo', methods=['POST'])
@check_token
def create(token):
    data = request.get_json()
    entry = Todo(
        summary=data['summary'], 
        description=data['description'],
        status='New',
        user_id=token.user_id
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify({'id': entry.id})


@bp.route('/todo/<todo_id>', methods=['GET'])
@check_token
def get(token, todo_id):
    item = Todo.query.get(todo_id)
    if item is None:
        return ('', 404)
    elif item.user_id != token.user_id:
        return ('', 404)
    else:
        return jsonify(item.serialize())


@bp.route('/todo', methods=['GET'])
@check_token
def list_all(token):
    todo_list = Todo.query.filter_by(user_id=token.user_id).all()
    return jsonify([i.serialize() for i in todo_list])


@bp.route('/todo/<todo_id>', methods=['DELETE'])
@check_token
def delete(token, todo_id):
    item = Todo.query.get(todo_id)
    if token.user_id == item.user_id:
        db.session.delete(item)
        db.session.commit()
        return ('', 204)
    else:
        return ('', 404)


@bp.route('/todo/<todo_id>', methods=['PATCH'])
@check_token
def update_status(token, todo_id):
    item = Todo.query.get(todo_id)
    if token.user_id == item.user_id:
        data = request.get_json()
        if item.merge_update(data) is True:
            db.session.commit()
            return ('', 204)
        else:
            return (jsonify({'error': 'Invalid data sent.'}), 400)
    else:
        return ('', 404)

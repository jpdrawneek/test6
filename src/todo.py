from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src import db
from src.model import User, Todo, AuthToken

bp = Blueprint('todo', __name__, url_prefix='/api')

@bp.route('/todo', methods=['POST'])
def create():
    data = request.get_json()
    entry = Todo(
        summary=data['summary'], 
        description=data['description'],
        status='New',
        user_id=1
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify({'id': entry.id})


@bp.route('/todo/<todo_id>', methods=['GET'])
def get(todo_id):
    item = Todo.query.get(todo_id)
    return jsonify(item)


@bp.route('/todo', methods=['GET'])
def list_all():
    list = Todo.query.filter_by(user_id=1)
    return jsonify(list)


@bp.route('/todo/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    item = Todo.query.get(todo_id)
    db.session.delete(item)
    db.session.commit()
    return ('', 204)


@bp.route('/todo/<todo_id>', methods=['PATCH'])
def update_status(todo_id):
    item = Todo.query.get(todo_id)
    data = request.get_json()
    item.merge_update(data)
    db.session.commit()
    return ('', 204)

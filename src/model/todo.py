"""
Model definition for todo data type.
"""

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User',
        backref=db.backref('todos', lazy=True))

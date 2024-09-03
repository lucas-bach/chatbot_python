from flask import Blueprint,request,jsonify
from models import Task,User
from extensions import db
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

task_bp = Blueprint('task_bp',__name__,)


@task_bp.route('/tasks',methods=['POST'])
@jwt_required()

def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'],description=data.get['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201


@task_bp.route('/tasks',methods=['GET'])
@jwt_required()

def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@task_bp.route('/tasks/<int:id>',methods=['GET'])
@jwt_required()

def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()), 200


@task_bp.route('/tasks/<int:id>',methods=['PUT'])
@jwt_required()

def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data['title']
    task.description = data.get('description')
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify(task.to_dict()), 200


@task_bp.route('/tasks/<int:id>',methods=['DELETE'])
@jwt_required()

def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

@task_bp.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


@task_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({"error": "Invalid usrname or password"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
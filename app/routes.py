from flask import render_template, request, jsonify
from . import bp
from .models import Task, mongo, ObjectId

@bp.route('/')
def index():
    tasks = mongo.db.tasks.find()
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    status = request.form.get('status')
    task = {'title': title, 'status': status}
    mongo.db.tasks.insert_one(task)
    return jsonify({'result': 'Task added successfully'})

@bp.route('/update_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')

    task_id = ObjectId(task_id)
    
    mongo.db.tasks.update_one({'_id': task_id}, {'$set': {'title': title, 'status': status}})
    return jsonify({'result': 'Task updated successfully'})

@bp.route('/delete_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_id = ObjectId(task_id)
    
    mongo.db.tasks.delete_one({'_id': task_id})
    return jsonify({'result': 'Task deleted successfully'})

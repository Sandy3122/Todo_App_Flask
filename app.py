from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo, ObjectId
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'
mongo = PyMongo(app)

@app.route('/')
def index():
    tasks = mongo.db.tasks.find()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    status = request.form.get('status')
    task = {'title': title, 'status': status}
    mongo.db.tasks.insert_one(task)
    return jsonify({'result': 'Task added successfully'})

@app.route('/update_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = json.loads(request.data)
    title = data.get('title')
    status = data.get('status')
    
    # Convert the task_id string to ObjectId
    task_id = ObjectId(task_id)
    
    # Find and update the task in the database
    mongo.db.tasks.update_one({'_id': task_id}, {'$set': {'title': title, 'status': status}})
    return jsonify({'result': 'Task updated successfully'})

@app.route('/delete_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Convert the task_id string to ObjectId
    task_id = ObjectId(task_id)
    
    # Delete the task from the database
    mongo.db.tasks.delete_one({'_id': task_id})
    return jsonify({'result': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

# Import necessary modules and classes
from flask import render_template, request, jsonify
from . import bp
from .models import Task, mongo, ObjectId

# Define a route for the home page
@bp.route('/')
def index():
    # Retrieve all tasks from the MongoDB collection
    tasks = mongo.db.tasks.find()
    
    # Render the HTML template and pass the tasks to it
    return render_template('index.html', tasks=tasks)

# Define a route for adding a new task
@bp.route('/add_task', methods=['POST'])
def add_task():
    # Retrieve task details from the POST request form
    title = request.form.get('title')
    status = request.form.get('status')
    
    # Create a dictionary representing the new task
    task = {'title': title, 'status': status}
    
    # Insert the new task into the MongoDB collection
    mongo.db.tasks.insert_one(task)
    
    # Return a JSON response indicating success
    return jsonify({'result': 'Task added successfully'})

# Define a route for updating an existing task
@bp.route('/update_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    # Retrieve task details from the JSON data in the PUT request
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')

    # Convert the task ID to an ObjectId
    task_id = ObjectId(task_id)
    
    # Update the task in the MongoDB collection
    mongo.db.tasks.update_one({'_id': task_id}, {'$set': {'title': title, 'status': status}})
    
    # Return a JSON response indicating success
    return jsonify({'result': 'Task updated successfully'})

# Define a route for deleting a task
@bp.route('/delete_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Convert the task ID to an ObjectId
    task_id = ObjectId(task_id)
    
    # Delete the task from the MongoDB collection
    mongo.db.tasks.delete_one({'_id': task_id})
    
    # Return a JSON response indicating success
    return jsonify({'result': 'Task deleted successfully'})

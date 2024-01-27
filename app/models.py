# Import necessary modules and classes
from flask_pymongo import PyMongo
from bson import ObjectId  # Import ObjectId from bson module

# Create an instance of PyMongo
mongo = PyMongo()

# Define a Task class to represent tasks
class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status

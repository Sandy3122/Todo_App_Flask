from flask_pymongo import PyMongo
from bson import ObjectId  # Add this line

mongo = PyMongo()

class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status

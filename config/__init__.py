# Import necessary modules and classes
import os
from flask import Flask
from app.models import mongo

# Define a function to create a Flask application
def create_app():
    # Create an instance of the Flask application
    app = Flask(__name__)

    # Configure the MongoDB URI for the application
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'

    # Set the static URL path for serving static files
    app.config['static_url_path'] = '/static'  # Make sure this line is present

    # Initialize the Flask-MongoEngine extension with the app
    mongo.init_app(app)

    # Import and register the blueprint from the 'app' module
    from app import bp as app_bp
    app.register_blueprint(app_bp)

    # Return the configured Flask application
    return app

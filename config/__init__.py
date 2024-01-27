import os
from flask import Flask
from app.models import mongo

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'
    app.config['static_url_path'] = '/static'  # Make sure this line is present

    mongo.init_app(app)

    from app import bp as app_bp
    app.register_blueprint(app_bp)

    return app

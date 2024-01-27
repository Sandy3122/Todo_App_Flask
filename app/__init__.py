# Import necessary module and class
from flask import Blueprint

# Create a Flask Blueprint named 'bp'
bp = Blueprint('app', __name__, template_folder='templates', static_folder='static')

# Import the 'routes' module (assuming it contains the route definitions)
from . import routes

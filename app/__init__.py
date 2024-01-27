# app/__init__.py
from flask import Blueprint

bp = Blueprint('app', __name__, template_folder='templates', static_folder='static')

from . import routes

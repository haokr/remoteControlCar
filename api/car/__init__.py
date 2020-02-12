from flask import Blueprint

car = Blueprint('car', __name__)

from . import view
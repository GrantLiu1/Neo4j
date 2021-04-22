from flask import Blueprint

user = Blueprint("user", __name__)

from .views import *
from .views1 import *
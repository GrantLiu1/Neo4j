from flask import Blueprint

relationship = Blueprint("relationship", __name__)

from .personRelationViews import *
from .testviews import *


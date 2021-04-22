from flask import Blueprint

node = Blueprint("node", __name__)

from .personViews import *
from .addressViews import *
from .companyViews import *

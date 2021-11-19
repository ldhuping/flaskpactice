from flask import Blueprint

practice01 = Blueprint('practice01', __name__,template_folder='templates')

from flaskpractice01.views import *
from flaskpractice01.models import *


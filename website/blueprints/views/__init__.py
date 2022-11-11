from flask import Blueprint
bp=Blueprint('views', __name__, url_prefix="/views")
from . import views

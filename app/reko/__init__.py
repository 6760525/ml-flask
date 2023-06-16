from flask import Blueprint

bp = Blueprint('reko', __name__)


from app.reko import routes
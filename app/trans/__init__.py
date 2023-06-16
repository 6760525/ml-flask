from flask import Blueprint

bp = Blueprint('trans', __name__)


from app.trans import routes
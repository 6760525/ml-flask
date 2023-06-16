from flask import render_template
from app.trans import bp

@bp.route('/')
def index():
    return render_template('trans/index.html')

@bp.route('/trans/')
def trans():
    return render_template('trans/translations.html')


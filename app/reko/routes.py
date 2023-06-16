from flask import render_template
from app.reko import bp

@bp.route('/')
def index():
    return render_template('reko/index.html')

@bp.route('/images/')
def images():
    return render_template('reko/images.html')

@bp.route('/faces/')
def faces():
    return render_template('reko/faces.html')

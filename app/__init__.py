from flask import Flask
from config import Config
from app.extensions import aws

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    #aws.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.reko import bp as reko_bp
    app.register_blueprint(reko_bp, url_prefix='/reko')

    from app.trans import bp as trans_bp
    app.register_blueprint(trans_bp, url_prefix='/trans')

    return app
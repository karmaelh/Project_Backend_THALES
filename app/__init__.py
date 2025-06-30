from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from .models import User
        db.create_all()

    # Importer les routes ici
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    @app.route('/')
    def home():
        return "Welcome to the Training API !!!!!!"

    return app

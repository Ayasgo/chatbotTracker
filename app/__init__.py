from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Import and register Blueprints
    from .views import main
    app.register_blueprint(main)

    return app

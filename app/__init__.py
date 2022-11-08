from flask import Flask
import logging
import click
import os
from .cli import register_cli
from .extensions import db, DB_NAME, login_manager

def create_app():
    # Create app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev' # Key used to encrypt data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    register_extensions(app)
    register_cli(app)

    # Setting up views and blueprints
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    # Create data base
    from .models import User, Note
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
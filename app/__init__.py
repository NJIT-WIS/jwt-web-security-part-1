"""A simple flask web app"""

import flask_login
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from app.authentication import authentication
from app.db import db, database
from app.db.models import User
from app.logging_config import logging_config


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")
    # gets the login manager to manage logged-in users
    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    # initializes the database connection for the app
    db.init_app(app)
    app.register_blueprint(database)
    app.register_blueprint(logging_config)
    app.register_blueprint(authentication)
    with app.app_context():
        jwt = JWTManager(app)

        @jwt.user_identity_loader
        def user_identity_lookup(user):
            return user

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            identity = jwt_data["sub"]
            return User.query.filter_by(username=identity).one_or_none()

    return app

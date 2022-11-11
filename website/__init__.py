from flask import Flask, render_template, request, url_for, redirect
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
login = LoginManager()


if os.environ.get('FLASK_DEBUG'):
    cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'ilmbjandtanda'
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    

    from .blueprints.views import bp as views_bp
    app.register_blueprint(views_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return render_template("home.html.j2")


    return app
from website import models


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path

# db = SQLAlchemy()
# DB_NAME = "database.db"


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'ilmbjandtanda'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     db.init_app(app)

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')

#     from .models import User, Note



#     return app




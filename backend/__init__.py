from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
#from flask_mail import Mail
from backend.config import Config
import requests


db = SQLAlchemy()
#bcrypt = Bcrypt()
#login_manager = LoginManager()
#login_manager.login_view = 'users.login'
#login_manager.login_message_category = 'info'
#mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="../dist") # needed in production only
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    #bcrypt.init_app(app)
    #login_manager.init_app(app)
    #mail.init_app(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')    # not clear why/if this is needed
    def catch_all(path):
        return render_template("index.html")

    from backend.games.routes import games
    app.register_blueprint(games)
    """
    from backend.users.routes import users
    from backend.posts.routes import posts
    from backend.main.routes import main
    from backend.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    """

    return app

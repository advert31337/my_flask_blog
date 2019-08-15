from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from src.config import Config

from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
admin = Admin()

# migrate = Migrate()
# manager = Manager()
# manager.add_command('db', MigrateCommand)
from src.models import *

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Tag, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))

    from .users.routes import users
    from .posts.routes import posts
    from .main.routes import main
    from .weather.routes import weather
    from .news.routes import news
    from .errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(weather)
    app.register_blueprint(news, url_prefix='/media')

    return app


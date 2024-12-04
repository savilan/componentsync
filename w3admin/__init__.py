from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oJew_hVN9dv46ZkLReHCVw'
    app.secret_key = 'oJew_hVN9dv46ZkLReHCVw'
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
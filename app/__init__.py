from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_message = "Please login!!"

    from .views import auth
    from .views import home

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(home, url_prefix='/')

    return app

db = SQLAlchemy()

app = create_app();

app.run(host='0.0.0.0', port=3000, debug=True)




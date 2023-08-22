from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_authorize import Authorize

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    from .views import auth
    from .views import home

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(home, url_prefix='/')

    return app

db = SQLAlchemy()

app = create_app();

login_manager = LoginManager(app)
login_manager.login_view = 'auth/login'

# authorize = Authorize(app)

app.run(host='0.0.0.0', port=3000, debug=True)




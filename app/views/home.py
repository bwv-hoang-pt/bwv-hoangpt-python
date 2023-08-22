
from flask import Blueprint, render_template
from flask_login import LoginManager
from app.models.user import User

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/index')
def index():
    return render_template('home.html')
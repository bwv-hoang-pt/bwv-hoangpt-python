from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user
from sqlalchemy import or_
from app import forms, db
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('home.index'))
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form=forms.RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user=User.query.filter(or_(
                User.username==form.username.data, 
                User.email==form.email.data
            )).first()
            if user:
                flash('Username or email is already registered')
                return redirect(url_for('auth.register'))
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

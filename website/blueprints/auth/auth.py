from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp as auth
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm



#auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # LOGIN THE USER HERE
        email = form.email.data.lower()
        password = form.password.data
                                #colname = value
        u = User.query.filter_by(email=email).first()
        if u and u.check_hashed_password(password):
            #Login Success!!!!
            flash('Successfully Logged in', 'success')
            login_user(u)
            return redirect(url_for('index'))
       
        error_string = "Incorrect Email/Password Combo"
        return render_template('login.html', loginerror=error_string, form=form)
    return render_template('login.html', form=form)
# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     login = 'hello'
#     if request.method == 'POST' and form.validate_on_submit():
#         email = form.email.data.lower()
#         password = form.password.data

#         u = User.query.filter_by(email=email).first()
        
#         login_user(u)
#         return redirect(url_for("index"))
#     return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        Name = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error') 
        elif len(Name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            flash('Account created!', category='success')
            

    return render_template("sign-up.html")

    

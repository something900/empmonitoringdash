from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #check if user is valid
        user = User.query.filter_by(email=email).first()
        #if there is a user
        if user:
            #accesss the user.pasword and check if its same as password typed
            if check_password_hash(user.password, password):
                flash('LOGIN SUCCESS', category='success')
                #remember user infor till session is cleared
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again',category='error')

        else:
            flash('Email does not exsist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #to make sure pre exsisting users dont register again
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        else:
            new_user = User(email=email,
            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(user, remember=True)

            flash('Account created!', category='success')
            #if sgnup is successful then redirect to home page
            return redirect(url_for('views.home'))


    return render_template("signup.html", user=current_user)
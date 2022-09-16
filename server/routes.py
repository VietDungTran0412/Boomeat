import os
from flask import flash, render_template, url_for, request, redirect
from server import app, bcrypt, db
from server.form_validation import RegisterValidation
from server.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('index.html',nav_bar=True,title='Boomeat')



@app.route('/register',methods=('POST','GET'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        address = request.form.get('address')
        zip = request.form.get('zip')
        city = request.form.get('city')
        age = request.form.get('age')
        password = request.form.get('password')
        remember = request.form.get('remember')
        validation = RegisterValidation(fname,lname,email,address,city,age,zip,password)
        if validation.validate_on_submit():
            if not User.query.filter_by(email=email).first():
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                new_user = User(fname = fname, lname = lname, email = email, city = city, zip_code = zip, password = hashed_password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                flash(f'Successfully created an acount for {fname} {lname}','success')
                return redirect(url_for('index'))
            else:
                flash(f'Email {email} already existed!','danger')
        else:
            flash(f'{validation.message}','danger')
    return render_template('register.html', title='Register',nav_bar = False)

@app.route('/login',methods=('POST','GET'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            flash(f'Welcome {user.fname} {user.lname}!','success')
            return redirect(url_for('index'))
    return render_template('login.html', title = 'Login', nav_bar = False)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
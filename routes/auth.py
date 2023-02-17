from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from db.User import User
from db.db import db
from forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__,
                 template_folder='templates')


# @auth.route('/authorization', methods=['GET', 'POST'])
# def authorization():
#     form = LoginForm()
#
#     return render_template('authorization.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        next_url = request.form.get("next")
        # print(next_url)
        if not password or not email:
            flash("Введите данные")
            return render_template('authorization.html', form=form)
        remember = True if request.form.get('rememberme') else False
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template('authorization.html', form=form)
        # flash("Успешная авторизация")
        login_user(user, remember=remember)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('index' ))
        #     print(next_url)
        #     # return redirect(url_for("profile"))
    return render_template('authorization.html', form=form,next=request.url)


# @auth.route('/registration', methods=['GET', 'POST'])
# def registration():
#     return render_template('registration.html')
# Update query
# with app.test_request_context():
# print (post_counter())
# print(delete(1))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user:
            flash("С таким email пользователь уже существует")
            return render_template('registration.html', form=form)
        if request.form.get('password') == request.form.get('passwordrpt'):
            hash = generate_password_hash(request.form.get('password'))
            new_user = User(name=request.form.get('name'), email=request.form.get('email'), password=hash)
            db.session.add(new_user)
            db.session.commit()
            flash("Успешная регистрация")
            print("ok")
            return redirect(url_for('auth.login'))
        else:
            flash("Ошибка регистрации")
            print("Nok")
        return render_template('registration.html', form=form)
    return render_template('registration.html', form=form)

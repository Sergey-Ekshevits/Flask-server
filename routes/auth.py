from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from db.User import User
from db.db import db

auth = Blueprint('auth', __name__,
                 template_folder='templates')


@auth.route('/authorization', methods=['GET', 'POST'])
def authorization():
    return render_template('authorization.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    email = request.form.get('email')
    password = request.form.get('psw')
    if not password or not email:
        flash("Введите данные")
        return redirect(url_for('auth.authorization'))
    remember = True if request.form.get('remainme') else False
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.authorization'))
    flash("Успешная авторизация")
    login_user(user, remember=remember)
    return redirect(request.args.get("next") or url_for('index'))


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html')
    # Update query
    # with app.test_request_context():
    # print (post_counter())
    # print(delete(1))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.authorization"))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if len(request.form['user_name']) > 3 and len(request.form['email']) > 4 and request.form['psw'] == \
                request.form['pswrpt']:
            hash = generate_password_hash(request.form['psw'])
            db.session.add(User(name=request.form['user_name'], email=request.form['email'], password=hash))
            db.session.commit()
            flash("Успешная регистрация")
            print("ok")
            return redirect(url_for('auth.authorization'))
        else:
            flash("Ошибка регистрации")
            print("Nok")
        return render_template('registration.html')

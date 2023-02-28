from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from db.User import User
from db.Post import Post
from db.db import db
from forms import LoginForm, RegisterForm, ChangeProfileForm
from functions import upload_avatar


auth = Blueprint('auth', __name__,
                 template_folder='templates')

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
        login_user(user, remember=remember)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('index'))
    return render_template('authorization.html', form=form, next=request.url)

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
            login_user(new_user, remember=True)
            return redirect(url_for('index'))
        else:
            flash("Ошибка регистрации")
            print("Nok")
        return render_template('registration.html', form=form)
    return render_template('registration.html', form=form)


@auth.route('/profile')
def profile():
    user_posts = db.session.query(Post).join(User).filter(Post.owner == current_user.id).all()
    return render_template("profile.html", user_posts=user_posts, current_user=current_user)


@auth.route('/change_profile/<int:id>', methods=['GET', 'POST'])
def change_profile(id):
    updated_user = User.query.get_or_404(id)
    form = ChangeProfileForm(name=current_user.name)
    if request.method == 'POST' and form.validate_on_submit:
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filename = upload_avatar(file, updated_user)
                updated_user.avatar_url = filename
        updated_user.name = request.form.get("name")
        try:
            db.session.commit()
            return redirect(url_for("auth.profile"))
        except:
            flash("Данные не сохранились")
    return render_template("change_profile.html", current_user=current_user, id=id, form=form)


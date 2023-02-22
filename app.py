import os
from datetime import datetime

from flask import Flask
from flask import render_template, request, redirect, g, url_for
from database import *
from flask_login import LoginManager, current_user, login_required
from forms import SearchForm
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_paginate import Pagination, get_page_parameter, get_page_args
from db.Post import Post
from db.db import db
from db.User import User
from routes.auth import auth
from routes.posts import post

DATABASE = 'blogdb.db'
DATABASE2 = 'blogdb2.db'
DEBUG = False
SECRET_KEY = '239184u0dasfdasgert3243dfasdfAW32%^'
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(post)
# sess = session()
app.config.update(dict(DATABASE=os.path.join(app.root_path, DATABASE)))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(app.root_path, DATABASE2)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message='Авторизуйтесь для доступа к странице'
login_manager.login_message_category='success'
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
POSTS_PER_PAGE = 4
# db.create_all()
# db.session.add(User(name='john', email='jd@example.com', password='Biology student'))
# db.session.commit()

# def connect_db():
#     conn=sqlite3.connect(app.config['DATABASE'])
#     conn.row_factory = sqlite3.Row
#     return conn

# def create_db():
#     db = connect_db(app)
#     with app.open_resource('sqlq.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#     db.close()

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db(app)
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', menu=menu, title='Страница не найдена')


@app.errorhandler(504)
def page_not_found2(error):
    return render_template('404.html', menu=menu, title='Страница не найдена')


menu = [
    {
        "name": "Главная",
        "link": "/"
    },
    {
        "name": "О нас",
        "link": "/"
    },
    {
        "name": "Авторизация",
        "link": "/authorization"
    }
]
@app.context_processor
def base():
    search_form=SearchForm()
    return dict(search_form=search_form)
@app.route('/', methods=['GET'])
# @app.route('/<int:page>', methods = ['GET', 'POST'])
# @login_required
def index():
    # pag={}
    content={}
    page = request.args.get('page', 1, type=int)
    print(page)
    # posts=Post.query.all()
    # posts=Post.query.paginate(1,3)
    pagination = Post.query.paginate(page=page, per_page=POSTS_PER_PAGE)
    content['pagination'] = Pagination(page=page, total=11,
                                       per_page=POSTS_PER_PAGE, bs_version=4)
    # pag["pagin"] = Pagination(page=page, total=pagination)
    print(pagination)
    # posts = db.session.query(Post).all()
    # posts2 = db.session.query(Post).join(User).filter(Post.owner == current_user.id).all()
    # test = db.session.query(User, Post).filter(Post.owner == current_user.id).all()

    # print(posts2)
    # page = request.args.get('page')
    # posts = getAllPosts(db, page)
    return render_template(
        'index.html',
        # posts=posts,
        current_user=current_user,
        # post_counter=post_counter(db),
        title="Блог",
        menu=menu,
        pagination = pagination
    )
@app.route('/search', methods=['GET'])
def search():
    searched=request.args.get('search_field')
    posts=[]
    if searched:
        posts=Post.query.filter(Post.body.contains(searched) | Post.title.contains(searched)).order_by(Post.title).all()
    return render_template("search_result.html",searched=searched,posts=posts)


# @app.route('/delete/<id>')
# def delete(id):
#     db = get_db()
#     delete_post(db, id)
#     # cursor.execute('SELECT * FROM posts WHERE id=?', [id])
#     # req=cursor.fetchone()['id']
#     return redirect(url_for('index'))


# @app.route('/post/<id>')
# # @login_required
# def post(id):
#     db = get_db()
#     post = get_post(db, id)
#     return render_template('post.html', post=post, menu=menu)


# @app.route('/create_post', methods=['POST'])
# def create_post():
#     db = get_db()
#     print(request.form)
#     header = request.form.get('header')
#     body = request.form.get('body')
#     id = request.form.get('id')
#     create_new_post(db, header, body)
#     print(id)
#     return redirect(url_for('index'))


# @app.route('/change_post', methods=['POST'])
# def change_post():
#     db = get_db()
#     # cursor = db.cursor()
#     # records=cursor.execute('SELECT * FROM posts')
#     # print(request.form)
#     # id = records.fetchall()[0][0]
#     new_header = request.form.get('header')
#     new_body = request.form.get('body')
#     id = request.form.get('id')
#     change_post_func(db, new_header, new_body, id)
#     # print (post)
#     # print (new_header,new_body)
#     # print (posts[0][0])
#     return redirect(url_for('index'))


# @app.route('/modify_post/<id>', methods=['GET'])
# @login_required
# def modify_post(id):
#     # db = get_db()
#     # post = get_post(db, id)
#     # print(request.form)
#     # new_header=request.form.get('header')
#     # new_body=request.form.get('body')
#     # change_post(new_header,new_body)
#
#     return render_template('change_post.html', post=post, menu=menu)




@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return datetime.fromtimestamp(int(value)).strftime(format)



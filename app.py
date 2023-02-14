from flask import Flask, session
from flask import render_template, request, redirect, g, url_for, flash, get_flashed_messages
import os
from database import *
from werkzeug.security import generate_password_hash, check_password_hash

from db.db import db
from db.User import User

DATABASE = 'blogdb.db'
DATABASE2 = 'blogdb2.db'
DEBUG = False
SECRET_KEY = '239184u0dasfdasgert3243dfasdfAW32%^'
app = Flask(__name__)

# sess = session()
app.config.update(dict(DATABASE=os.path.join(app.root_path, DATABASE)))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(app.root_path, DATABASE2)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
app.secret_key = SECRET_KEY

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


# def change_post_func(new_header, new_body, id):
#     db = get_db()
#     cursor = db.cursor()
#     query = "UPDATE posts SET header = ?, body = ? WHERE id = ?"
#     # id=2
#     # Values to update
#     values = (new_header, new_body, id)
#
#     # Execute the update query
#     cursor.execute(query, values)
#
#     # Commit the changes
#     db.commit()
#  # db.close()

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

@app.route('/')
def index():
    db = get_db()
    page = request.args.get('page')
    # print(page)
    posts = getAllPosts(db, page)
    return render_template('index.html', posts=posts, post_counter=post_counter(db), title="Блог", menu=menu)


@app.route('/delete/<id>')
def delete(id):
    db = get_db()
    delete_post(db, id)
    # cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    # req=cursor.fetchone()['id']
    return redirect(url_for('index'))


# @app.route('/projects/')
# def projects():
#     return 'The project page'

@app.route('/post/<id>')
def post(id):
    db = get_db()
    post = get_post(db, id)
    return render_template('post.html', post=post, menu=menu)


@app.route('/create_post', methods=['POST'])
def create_post():
    db = get_db()
    print(request.form)
    header = request.form.get('header')
    body = request.form.get('body')
    id = request.form.get('id')
    create_new_post(db, header, body)
    print(id)
    return redirect(url_for('index'))


@app.route('/change_post', methods=['POST'])
def change_post():
    db = get_db()
    # cursor = db.cursor()
    # records=cursor.execute('SELECT * FROM posts')
    # print(request.form)
    # id = records.fetchall()[0][0]
    new_header = request.form.get('header')
    new_body = request.form.get('body')
    id = request.form.get('id')
    change_post_func(db, new_header, new_body, id)
    # print (post)
    # print (new_header,new_body)
    # print (posts[0][0])
    return redirect(url_for('index'))


@app.route('/modify_post/<id>', methods=['GET'])
def modify_post(id):
    db = get_db()
    post = get_post(db, id)
    # print(request.form)
    # new_header=request.form.get('header')
    # new_body=request.form.get('body')
    # change_post(new_header,new_body)

    return render_template('change_post.html', post=post, menu=menu)

@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    return render_template('authorization.html', menu=menu)
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html', menu=menu)
    # Update query
    # with app.test_request_context():
    # print (post_counter())
    # print(delete(1))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        if len(request.form['user_name'])>3 and len(request.form['email'])>4 and request.form['psw'] == request.form['pswrpt']:
            hash=generate_password_hash(request.form['psw'])
            #add user method
            flash("Успешная регистрация")
            print("ok")
            return redirect(url_for('authorization'))
        else:
            flash("Ошибка регистрации")
            print("Nok")
        return render_template('registration.html', menu=menu)
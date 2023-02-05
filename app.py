from flask import Flask
from markupsafe import escape
from flask import render_template, request, redirect, g, url_for
import os
from database import connect_db, post_counter, getAllPosts, create_new_post, change_post_func, delete_post

DATABASE = 'blogdb.db'
DEBUG = False
SECRET_KEY ='239184u0dasfdasgert3243dfasdfAW32%^'

app = Flask(__name__)
app.config.update(dict(DATABASE = os.path.join(app.root_path,'blogdb.db')))

# def connect_db():
#     conn=sqlite3.connect(app.config['DATABASE'])
#     conn.row_factory = sqlite3.Row
#     return conn

def create_db():
    db=connect_db(app)
    with app.open_resource('sqlq.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g,'link_db'):
        g.link_db = connect_db(app)
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()
# create_db()
# cursor = get_db().cursor()
# create_db()
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("База данных создана и успешно подключена к SQLite")


# with sqlite3.connect('sqlite_python.db', check_same_thread=False) as db:
#     db.row_factory = sqlite3.Row
#     cursor = db.cursor()

# sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS posts (
#                                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                     header TEXT NOT NULL,
#                                     body TEXT NOT NULL,
#                                     timestamp DATATIME DEFAULT CURRENT_TIMESTAMP
#                                     );'''

# cursor.execute(sqlite_create_table_query)
# record = cursor.fetchall()
# print("Версия базы данных SQLite: ", record)
# cursor.close()


# # except sqlite3.Error as error:
# # print("Ошибка при подключении к sqlite", error)
# # finally:
# #     if (sqlite_connection):
# #         sqlite_connection.close()
# #         print("Соединение с SQLite закрыто")

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
#     # db.close()


menu = ['Главная', 'Купить этот сайт', 'О нас']


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
    delete_post(db,id)
    # cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    # req=cursor.fetchone()['id']
    return redirect(url_for('index'))


# @app.route('/projects/')
# def projects():
#     return 'The project page'

@app.route('/post/<id>')
def post(id):
    db = get_db()
    # post = getPost(db, id) // надо сделать
    cursor = db.cursor()
    res = cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    post = res.fetchone()
    print(post)
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
    change_post_func(db,new_header, new_body, id)
    # print (post)
    # print (new_header,new_body)
    # print (posts[0][0])
    return redirect(url_for('index'))


@app.route('/modify_post/<id>', methods=['GET'])
def modify_post(id):
    db = get_db()
    cursor = db.cursor()
    res = cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    post = res.fetchone()
    # print(request.form)
    # new_header=request.form.get('header')
    # new_body=request.form.get('body')
    # change_post(new_header,new_body)
    print('test')
    return render_template('change_post.html', post=post, menu=menu)

    # Update query
    # with app.test_request_context():
        # print (post_counter())
        # print(delete(1))

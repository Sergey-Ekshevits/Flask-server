from flask import Flask
from markupsafe import escape
from flask import render_template, request, redirect

import sqlite3

with sqlite3.connect('sqlite_python.db', check_same_thread=False) as db:
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("База данных создана и успешно подключена к SQLite")

sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS posts (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    header TEXT NOT NULL,
                                    body TEXT NOT NULL,
                                    timestamp DATATIME DEFAULT CURRENT_TIMESTAMP
                                    );'''

cursor.execute(sqlite_create_table_query)
# record = cursor.fetchall()
# print("Версия базы данных SQLite: ", record)
# cursor.close()


# except sqlite3.Error as error:
# print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")
app = Flask(__name__)


def create_new_post(header, body):
    sqlite_insert_query = """INSERT INTO posts
                          (header,body)
                          VALUES
                          (?,?);"""

    # Close the connection
    # db.close()

    cursor.execute(sqlite_insert_query, [header, body])
    db.commit()
    # db.close()


def post_counter(posts):
    record = cursor.execute('SELECT * FROM posts')
    posts = record.fetchall()
    counter = len(posts)
    return counter


def change_post_func(new_header, new_body, id):
    query = "UPDATE posts SET header = ?, body = ? WHERE id = ?"
    # id=2
    # Values to update
    values = (new_header, new_body, id)

    # Execute the update query
    cursor.execute(query, values)

    # Commit the changes
    db.commit()
    # db.close()


menu = ['Главная', 'Купить этот сайт', 'О нас']


@app.route('/')
def index():
    record = cursor.execute('SELECT * FROM posts')
    posts = record.fetchall()
    # array=[]
    # print(posts)
    # for post in posts:
    #     dict={
    #         "id":post[0],
    #         "header":post[1],
    #         "body":post[2],
    #         "timestamp":post[3],
    #     }
    #     array.append(dict)
    # print(post_counter(posts))
    # post_counter(posts)
    return render_template('index.html', posts=posts, title="Блог", menu=menu)


@app.route('/delete/<id>')
def delete(id):
    cursor.execute('DELETE FROM posts WHERE id=?', [id])
    return redirect('/')


# @app.route('/projects/')
# def projects():
#     return 'The project page'

@app.route('/post/<id>')
def post(id):
    res = cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    post = res.fetchall()
    print(post)
    return render_template('post.html', post=post, menu=menu)


@app.route('/create_post', methods=['POST'])
def create_post():
    print(request.form)
    header = request.form.get('header')
    body = request.form.get('body')
    id = request.form.get('id')
    create_new_post(header, body)
    print(id)
    return redirect('/')


@app.route('/change_post', methods=['POST'])
def change_post():
    # records=cursor.execute('SELECT * FROM posts')
    # print(request.form)
    # id = records.fetchall()[0][0]
    new_header = request.form.get('header')
    new_body = request.form.get('body')
    id = request.form.get('id')
    change_post_func(new_header, new_body, id)
    # print (post)
    # print (new_header,new_body)
    # print (posts[0][0])
    return redirect('/')


@app.route('/modify_post/<id>', methods=['GET'])
def modify_post(id):
    res = cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    post = res.fetchall()
    print(request.form)
    # new_header=request.form.get('header')
    # new_body=request.form.get('body')
    # change_post(new_header,new_body)
    return render_template('change_post.html', post=post, menu=menu)

    # Update query

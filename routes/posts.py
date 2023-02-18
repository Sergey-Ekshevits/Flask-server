import calendar
import time

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import select, update, delete, values

from db.Post import Post
from db.db import db

post = Blueprint('post', __name__,
                 template_folder='templates')


@post.route('/create_post', methods=['POST'])
def create_post():
    print(current_user.id)
    header = request.form.get('header')
    body = request.form.get('body')
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    post = Post(title=header, body=body, owner=current_user.id, date_created=time_stamp)
    db.session.add(post)
    db.session.commit()
    # print(post)
    return redirect(url_for('index'))


@post.route('/post/<id>')
def show_post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)
@post.route('/delete/<id>')
def delete_post(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))

@post.route('/change_post/<id>', methods=['GET','POST'])
@login_required
def change_post(id):
    post = Post.query.filter_by(id=id).first()
    # print(post.title)
    if request.method == "POST":
        new_header = request.form.get('title')
        new_body = request.form.get('body')
        # id = request.form.get('id')
        # print(id)
        # post=Post.query.filter_by(id=id).first
        Post.query.filter_by(id=id).update({
        Post.title: new_header,
        Post.body:  new_body
        })

        # Post.query.filter_by(id=id).update({
        #     Post.title: new_header,
        #     Post.body: new_body
        # })
        print(post.title)
        print(post.body)
        # print(post.id)
        db.session.commit()
        # change_post_func(db, new_header, new_body, id)
        # print (post)
        # print (new_header,new_body)
        # print (posts[0][0])
        return redirect(url_for('index'))
    return render_template('change_post.html',post=post)

# def change_post_func(db, new_header, new_body, id):
#     cursor = db.cursor()
#     query = "UPDATE posts SET header = ?, body = ? WHERE id = ?"
#     # Values to update
#     values = (new_header, new_body, id)
#     # Execute the update query
#     cursor.execute(query, values)
#     # Commit the changes
#     db.commit()
#     # db.close()

# @app.route('/modify_post/<id>', methods=['GET'])
# @login_required
# def modify_post(id):
#     db = get_db()
#     post = get_post(db, id)
#     # print(request.form)
#     # new_header=request.form.get('header')
#     # new_body=request.form.get('body')
#     # change_post(new_header,new_body)
#     return render_template('change_post.html', post=post, menu=menu)
import calendar
import time
from db.UserTelegram import UserTelegram

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import select, update, delete, values
from forms import PostField
from db.Post import Post
from db.db import db
from bot import bot
post = Blueprint('post', __name__,
                 template_folder='templates')


# @post.route('/create_post', methods=['POST'])
# def create_post():
#     print(current_user.id)
#     header = request.form.get('header')
#     body = request.form.get('body')
#     current_GMT = time.gmtime()
#     time_stamp = calendar.timegm(current_GMT)
#     post = Post(title=header, body=body, owner=current_user.id, date_created=time_stamp)
#     db.session.add(post)
#     db.session.commit()
#     # print(post)
#     return redirect(url_for('index'))
@post.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostField()
    if request.method == "POST":
        header = request.form.get('title')
        body = request.form.get('body')
        if len(body) <= 20:
            flash("Текст поста должен быть больше...")
            return render_template('add_post.html', form=form)
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        allTgUsers = UserTelegram.query.all()
        for tgUser in allTgUsers:
            print(tgUser)
            bot.send_message(tgUser.user_id, "Новый пост создал " + current_user.name + ". Заголовок поста - " + header , 
                         parse_mode='Markdown')
        post = Post(title=header, body=body, owner=current_user.id, date_created=time_stamp)
        db.session.add(post)
        db.session.commit()

        # sendMessage()
        return redirect(url_for("index"))
    return render_template('add_post.html', form=form)

@post.route('/post/<id>')
def show_post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)
@post.route('/delete/<id>')
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post and current_user.id == post.user.id:
        Post.query.filter_by(id=id).delete()
        db.session.commit()
    return redirect(url_for('index'))


@post.route('/change_post/<id>', methods=['GET','POST'])
@login_required
def change_post(id):
    form = PostField()
    post = Post.query.filter_by(id=id).first()
    form.title.data = post.title
    form.body.data = post.body
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    # print(post.title)
    if current_user.id == post.user.id and request.method == "POST":
        new_title = request.form.get('title')
        new_body = request.form.get('body')
        Post.query.filter_by(id=id).update({
            Post.title: new_title,
            Post.body: new_body,
            Post.date_modified: time_stamp
        })
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('change_post.html',post=post, form=form)
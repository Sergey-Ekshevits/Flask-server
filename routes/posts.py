import calendar
import time
from db.UserTelegram import UserTelegram

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import select, update, delete, values
from forms import PostField, CommentField
from db.Post import Post
from db.Comments import Comments
from db.db import db
from bot import bot
from functions import upload_pic, delete_file
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
    if request.method == "POST" and form.validate_on_submit:
        header = request.form.get('title')
        body = request.form.get('body')
        post_pic = upload_pic(request.files['post_pic'],folder='post-picture')
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
        post = Post(title=header, body=body, owner=current_user.id, date_created=time_stamp, post_pic=post_pic)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            flash("Данные не сохранились")
    return render_template('add_post.html', form=form)

@post.route('/post/<id>',methods=['GET', 'POST'])
def show_post(id):
    form = CommentField()
    post = Post.query.filter_by(id=id).first()
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    comments = post.comments
    if request.method=='POST' and form.validate_on_submit():
        comment=Comments(content = request.form.get('content'), commentator=current_user.id, date_created = time_stamp, commented_post = post.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post.show_post',id=post.id))
    return render_template('post.html', post=post, comments=comments,form=form)

@post.route('/delete_comment/<id>')
def delete_comment(id):
    comment = Comments.query.filter_by(id=id).first()
    post_id=comment.commented_post
    if int(comment.commentator) == current_user.id:
        print(comment.commentator, current_user.id, id)
        Comments.query.filter_by(id=id).delete()
        db.session.commit()
    else:
        print("Failed")
    return redirect(url_for('post.show_post', id=post_id))
@post.route('/delete/<id>')
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    post_pic = post.post_pic
    if post and current_user.id == post.user.id:
        if post_pic:
            delete_file(post_pic, folder="post-picture")
        Post.query.filter_by(id=id).delete()
        db.session.commit()
    return redirect(request.referrer)


@post.route('/change_post/<id>', methods=['GET','POST'])
@login_required
def change_post(id):
    form = PostField()
    post = Post.query.filter_by(id=id).first()
    form.title.data = post.title
    form.body.data = post.body
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
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
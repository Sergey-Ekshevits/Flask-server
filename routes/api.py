import calendar
import time

from flask import Blueprint, request, send_file
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash

# from db.UserTelegram import UserTelegram
from db.User import User
from db.db import db
from db.Post import Post
# from db.Category import Category
from db.Comments import Comments
from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
# from sqlalchemy_serializer import SerializerMixin
from functions import delete_file, upload_pic

api = Blueprint('api', __name__, url_prefix='/api',
                subdomain=None,
                template_folder='..\\client\\build',
                url_defaults=None,
                root_path=None,
                static_folder='..\\client\\build\\static',
                static_url_path='..\\client\\build\\static')


@api.route("/", defaults={'path': ''})
def serve(path):
    return send_file('client/build/index.html')


# @api.route("/static/<path>")
# def serve_static(path):
#     print(path)
#     print(213123123)
#     # pdb.set_trace()
#     print(api.static_folder + "\\" + path)
#     return api.send_static_file(api.static_folder + "\\" + path)


@api.route("/static/js/<path>")
def serve_js(path):
    return send_file(api.static_folder + "\\js\\" + path)


@api.route("/static/css/<path>")
def serve_css(path):
    return send_file(api.static_folder + "\\css\\" + path)


#  not need
@api.get('/serialized')
@jwt_required()
def get_posts2():
    result = []
    posts = Post.query.all()
    # post_scheme = PostScheme()
    # output = post_scheme.dump(posts)
    # print(post_scheme)
    for one_post in posts:
        post_dict = {
            "title": one_post.title,
            "id": one_post.id,
            "body": one_post.body,
            "post_pic": one_post.post_pic,
            "date_created": one_post.date_created,
            "user": {
                "name": one_post.user.name,
                "id": one_post.user.id,
                "avatar_url": one_post.user.avatar_url,
                "email": one_post.user.email
            }
        }
        result.append(post_dict)
    return jsonify(result)


@api.get('/posts')
@jwt_required()
def get_posts():
    post = Post.query.all()
    c = [c.to_dict() for c in post]
    return jsonify(c)


@api.post('/post/<id>')
@jwt_required()
def get_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        return jsonify(post.to_dict())
    return jsonify({"msg": "Нет поста по такому id"}), 404


@api.delete('/post/<id>')
@jwt_required()
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        if post.post_pic:
            delete_file(post.post_pic, folder="post-picture")
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({id: post.id})
    return jsonify({id: post.id}), 404


@api.patch('/post/<id>')
@jwt_required()
def update_post(id):
    post = Post.query.filter_by(id=id).first()
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    if post:
        post.title = request.form.get("title","")
        post.body = request.form.get("body","")
        pic = request.files.get("file")
        if pic:
            post.post_pic = upload_pic(pic, folder='post-picture', post=post)
        post.date_modified = time_stamp
        db.session.commit()
    return jsonify(post=post.to_dict())

@api.patch('/user')
@jwt_required()
def update_user():
    pass


@api.post('/comment')
@jwt_required()
def add_comment():
    pass


@api.post('/post')
@jwt_required()
def add_post():
    pass


@api.post('/registrate')
def registrate():
    data = request.json
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user:
        return jsonify({"msg": "Error on registration"}), 401
    hash = generate_password_hash(data["password"])
    new_user = User(name=data["name"], email=data["email"], password=hash)
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=data.get('email'))
    refresh_token = create_refresh_token(identity=data.get('email'))
    return jsonify(
        access_token=access_token,
        refresh_token=refresh_token,
        user=new_user.to_dict()
    )


@api.post("/login")
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)
    return jsonify(
        access_token=access_token,
        refresh_token=refresh_token,
        user={
            'name': user.name,
            'avatar_url': user.avatar_url,
            'email': user.email,
            'id': user.id
        }
    )


@api.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)


@api.post("/logout")
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

from flask import Blueprint, request
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from db.User import User
from db.db import db
from db.Post import Post
from flask import jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__, url_prefix='/api',
                template_folder='templates')


# @app.route('/modify', methods=['POST'])
# def modify():
#     posts_to_json = []
#     posts = Post.query.all()
#     for one_post in posts:
#         post_dict = {"title": one_post.title, "body": one_post.body}
#         posts_to_json.append(post_dict)
#     print(posts_to_json)
#     response = app.response_class(
#         response=json.dumps(posts_to_json),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
@api.get('/posts')
@jwt_required()
def get_posts():
    result = []
    posts = Post.query.all()
    for one_post in posts:
        post_dict = {
            "title": one_post.title,
            "body": one_post.body,
            "user": {
                "name": one_post.user.name,
                "id": one_post.user.id,
                "email": one_post.user.email
            }
        }
        result.append(post_dict)
    return jsonify(result)

@api.post('/registrate')
def registrate():
    data=request.json
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user:
        return jsonify({"error":"Error on registration"})
    hash = generate_password_hash(data["password"])
    new_user = User(name=data["name"], email=data["email"], password=hash)
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=data.get('email'))
    return jsonify(access_token=access_token, user={'name': user.name,'email':user.email,'id':user.id})

@api.post("/login")
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token, user={'name': user.name,'email':user.email,'id':user.id})
    return jsonify(access_token=access_token, user={'name': user.name,'email':user.email,'id':user.id})
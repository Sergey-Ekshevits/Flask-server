from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from db.db import db
from sqlalchemy_serializer import SerializerMixin

ass_post_category = db.Table(
    'ass_post_category',
    Column(
        'post_id',
        Integer,
        ForeignKey(
            'user_posts.id',
            ondelete='CASCADE')),
    Column(
        'category_id',
        Integer,
        ForeignKey(
            'post_category.id',
            ondelete='CASCADE'))
)


class Category(db.Model, SerializerMixin):
    __tablename__ = "post_category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<Category "{self.name}">'


class Comments(db.Model, SerializerMixin):
    __tablename__ = "post_comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    commentator = Column(String, ForeignKey('users.id'))
    date_created = Column(String, nullable=False)
    commented_post = Column(String, ForeignKey('user_posts.id'))


class Post(db.Model, SerializerMixin):
    __tablename__ = "user_posts"
    serialize_only = ()
    serialize_rules = (
        '-comments.post.comments',
        '-category.post')
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    body = Column(String, nullable=False)
    owner = Column(String, ForeignKey('users.id'))
    date_created = Column(String, nullable=False)
    date_modified = Column(String)
    user = db.relationship('User', backref='user_posts')
    comments = db.relationship('Comments', backref='post')
    post_pic = Column(String)
    category = db.relationship(
        'Category',
        secondary=ass_post_category,
        backref=db.backref("post",
                           cascade="all",
                           passive_deletes=True))


class User(UserMixin, db.Model, SerializerMixin):
    __tablename__ = "users"
    serialize_only = (
        'id',
        'name',
        'email',
        'avatar_url')
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    avatar_url = Column(String)
    posts = db.relationship('Post')
    user_comments = db.relationship(
        'Comments',
        backref='comment_owner')

    def __repr__(self):
        return f"{self.name}"


class UserTelegram(db.Model):
    __tablename__ = "user_telegram"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, unique=True)
    avatar_url = Column(String)

    def __repr__(self):
        return "<UserTelegram(name='%s', user_id='%s', avatar_url='%s')>" % (
            self.name,
            self.user_id,
            self.avatar_url,
        )

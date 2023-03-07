from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.db import db, ma
from sqlalchemy_serializer import SerializerMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
# from db.User import UserScheme

# post_category = db.Table('post_category',
#                     Column('post_id', Integer, ForeignKey('post.id')),
#                     Column('category_id', Integer, ForeignKey('category.id'))
#                     )
from db.post_category_table import ass_post_category

class Post(db.Model,SerializerMixin):
    __tablename__ = "user_posts"
    serialize_only = ()
    serialize_rules = ('-comments.post.comments','-category.post')
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    body = Column(String, nullable=False)
    owner = Column(String, ForeignKey('users.id'))
    date_created = Column(String, nullable=False)
    date_modified = Column(String)
    user = db.relationship('User', backref='user_posts')
    comments = db.relationship('Comments', backref='post')
    post_pic = Column(String)
    category = db.relationship('Category',secondary = ass_post_category, backref='post')

    # def __repr__(self):
    #     return "<User(name='%s', email='%s', password='%s')>" % (
    #         self.name,
    #         self.email,
    #         self.password,
    #     )

# class PostScheme(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Post
#         user = fields.Nested(UserScheme)


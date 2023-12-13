# from sqlalchemy import Column, Integer, String
# from sqlalchemy_serializer import SerializerMixin
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
# from db.db import db
# from flask_login import UserMixin
# # from db.Post import PostScheme
#
# class User(UserMixin, db.Model,SerializerMixin):
#     __tablename__ = "users"
#     serialize_only = ('id','name','email','avatar_url')
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String, unique=True)
#     password = Column(String)
#     avatar_url = Column(String)
#     posts = db.relationship('Post')
#     user_comments = db.relationship('Comments', backref='comment_owner')
#     def __repr__(self):
#         return "<User(name='%s', email='%s', password='%s')>" % (
#             self.name,
#             self.email,
#             self.password,
#         )
# # class UserScheme(SQLAlchemyAutoSchema):
# #     class Meta:
# #         model = User
# #         # posts = fields.Nested(PostScheme)
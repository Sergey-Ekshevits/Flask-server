# from sqlalchemy import Column, Integer, String, ForeignKey
# from db.db import db
# from sqlalchemy_serializer import SerializerMixin
# class Comments(db.Model,SerializerMixin):
#     __tablename__ = "post_comments"
#     # serialize_only = ('id',)
#     # serialize_rules = ('-commentator','-commented_post')
#     id = Column(Integer, primary_key=True)
#     content = Column(String, nullable=False)
#     commentator = Column(String, ForeignKey('users.id'))
#     date_created = Column(String, nullable=False)
#     commented_post = Column(String, ForeignKey('user_posts.id'))
#     # user = db.relationship('User', backref='commenter')
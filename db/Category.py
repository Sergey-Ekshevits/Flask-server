# from sqlalchemy import Column, Integer, String
# from db.db import db
# from sqlalchemy_serializer import SerializerMixin, Serializer
#
# class Category(db.Model,SerializerMixin):
#     __tablename__ = "post_category"
#     # serialize_only = ()
#     # serialize_rules = ('-ass_post_category',)
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f'<Category "{self.name}">'
#     # category_posts = Column(String, ForeignKey('user_posts.id'))
#     # user = db.relationship('User', backref='commenter')

from sqlalchemy import Column, Integer, String
from db.db import db


class Category(db.Model):
    __tablename__ = "post_category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<Category "{self.name}">'
    # category_posts = Column(String, ForeignKey('user_posts.id'))
    # user = db.relationship('User', backref='commenter')

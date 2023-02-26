from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, TIMESTAMP
from db.db import db


class Comment(db.Model):
    __tablename__ = "post_comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    commentator = Column(String, ForeignKey('users.id'))
    date_created = Column(String, nullable=False)
    commented_post = Column(String, ForeignKey('user_posts.id'))
    # user = db.relationship('User', backref='commenter')
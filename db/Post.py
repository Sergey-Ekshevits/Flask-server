from sqlalchemy import Column, Integer, String, ForeignKey
import User
from db.db import db


class Post(db.Model):
    __tablename__ = "user_posts"

    title = Column(String, unique=True)
    body = Column(String, nullable=False)
    owner = Column(String, ForeignKey('users.name'))
    # date_created =

    # def __repr__(self):
    #     return "<User(name='%s', email='%s', password='%s')>" % (
    #         self.name,
    #         self.email,
    #         self.password,
    #     )
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.db import db


class Post(db.Model):
    __tablename__ = "user_posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    body = Column(String, nullable=False)
    owner = Column(String, ForeignKey('users.id'))
    date_created = Column(String, nullable=False)

    # def __repr__(self):
    #     return "<User(name='%s', email='%s', password='%s')>" % (
    #         self.name,
    #         self.email,
    #         self.password,
    #     )
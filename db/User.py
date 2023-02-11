from sqlalchemy import Column, Integer, String
from db.db import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', email='%s', password='%s')>" % (
            self.name,
            self.email,
            self.password,
        )

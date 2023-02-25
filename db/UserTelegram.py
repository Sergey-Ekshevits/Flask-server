from sqlalchemy import Column, Integer, String
from db.db import db

class UserTelegram(db.Model):
    __tablename__ = "user_telegram"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, unique=True)
    avatar_url = Column(String)
    def __repr__(self):
        return "<User(name='%s', email='%s', password='%s')>" % (
            self.name,
            self.email,
            self.password,
        )

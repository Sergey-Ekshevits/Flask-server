from sqlalchemy import Column, Integer, String
from db.db import db
from sqlalchemy_serializer import SerializerMixin, Serializer
class UserTelegram(db.Model):
    __tablename__ = "user_telegram"
    # serialize_rules = ('-id',)
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, unique=True)
    avatar_url = Column(String)
    def __repr__(self):
        return "<UserTelegram(name='%s', user_id='%s', avatar_url='%s')>" % (
            self.name,
            self.user_id,
            self.avatar_url,
        )

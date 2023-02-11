# from sqlalchemy import Column, Integer, String
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# class User(db.Model):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
#
#     def __repr__(self):
#         return "<User(name='%s', email='%s', password='%s')>" % (
#             self.name,
#             self.email,
#             self.password,
#         )

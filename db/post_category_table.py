from db.db import db
from sqlalchemy import Column, Integer, String, ForeignKey

ass_post_category = db.Table('ass_post_category',
                    Column('post_id', Integer, ForeignKey('user_posts.id')),
                    Column('category_id', Integer, ForeignKey('post_category.id'))
                    )
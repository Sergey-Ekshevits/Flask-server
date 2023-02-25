import threading

import flask
from flask import current_app

from db.UserTelegram import UserTelegram
from db.db import db
from sqlalchemy.orm import scoped_session, sessionmaker


def add_user_telegram(message):
    print(message)
    # tr = threading.Thread(target=some_fynction)
    # tr.start()
    # with current_app.app_context():
    #     print(12312312)
    # tr2 = threading.enumerate()
    # print(tr)
    # print(tr2[2])

    # user_telegram = db.session.query(UserTelegram).filter_by(user_id=message.from_user.id).first()
    # db.session.query(UserTelegram)
    # user_telegram = UserTelegram.query.filter_by(user_id=message.from_user.id).first()
    # if not user_telegram:
    #     new_user_telegram = UserTelegram(user_id=message.from_user.id,
    #                                      name=message.from_user.first_name + " " + message.from_user.last_name)
    #     db.session.add(new_user_telegram)
    #     db.session.commit()


# def sendMessage():
#     bot.send_message("855830468", 'Пост создан ')

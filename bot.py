import telebot
from telebot import types
from db.UserTelegram import UserTelegram
from db.db import db

bot = telebot.TeleBot('5938142207:AAHiqSwhB-997sVsvWJ-mLSRfcbNnG71GlM', threaded=False)

bot.remove_webhook()
app_context = None

@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.id)
    add_user_telegram(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # print(message)

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)  # ответ бота


    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id,
                         'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)',
                         parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id,
                         'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)',
                         parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id,
                         'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)',
                         parse_mode='Markdown')


def run_bot(app_ctx):
    global app_context
    app_context = app_ctx
    bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть


def add_user_telegram(message):
    with app_context:
        user_telegram = UserTelegram.query.filter_by(user_id=message.from_user.id).first()
        if not user_telegram:
            new_user_telegram = UserTelegram(user_id=message.from_user.id,
                                            name=message.from_user.first_name + " " + message.from_user.last_name)
            db.session.add(new_user_telegram)
            db.session.commit()
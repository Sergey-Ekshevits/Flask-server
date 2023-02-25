from asyncio import sleep
import telebot
from telebot import types

BOT_TOKEN = "5300372542:AAE_XKXwURh4LoMB1R2Hf8anY7ptH24H4gY"
BOT_INTERVAL = 3
BOT_TIMEOUT = 30
bot = None

def bot_polling():
    #global bot #Keep the bot object as global variable if needed
    print("Starting bot polling now")
    while True:
        try:
            global bot
            print("New bot instance started")
            bot = telebot.TeleBot(BOT_TOKEN) #Generate new bot instance
            bot.remove_webhook()
            botactions(bot) #If bot is used as a global variable, remove bot as an input param
            bot.polling(none_stop=True, interval=BOT_INTERVAL, timeout=BOT_TIMEOUT)
        except Exception as ex: #Error in polling
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(BOT_TIMEOUT, ex))
            bot.stop_polling()
            sleep(BOT_TIMEOUT)
        else: #Clean exit
            bot.stop_polling()
            print("Bot polling loop finished")
            break #End loop

def botactions(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        print(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                        "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        print(message.text)
        print(message.from_user.id)
        if message.text == '👋 Поздороваться':
            markup = types.ReplyKeyboardMarkup(
                resize_keyboard=True)  # создание новых кнопок
            btn1 = types.KeyboardButton('Как стать автором на Хабре?')
            btn2 = types.KeyboardButton('Правила сайта')
            btn3 = types.KeyboardButton('Советы по оформлению публикации')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос',
                            reply_markup=markup)  # ответ бота

        elif message.text == 'Как стать автором на Хабре?':
            bot.send_message(message.from_user.id,
                            'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' +
                            '[ссылке](https://habr.com/ru/sandbox/start/)',
                            parse_mode='Markdown')

        elif message.text == 'Правила сайта':
            bot.send_message(message.from_user.id,
                            'Прочитать правила сайта вы можете по ' +
                            '[ссылке](https://habr.com/ru/docs/help/rules/)',
                            parse_mode='Markdown')

        elif message.text == 'Советы по оформлению публикации':
            bot.send_message(message.from_user.id,
                            'Подробно про советы по оформлению публикаций прочитать по ' +
                            '[ссылке](https://habr.com/ru/docs/companies/design/)',
                            parse_mode='Markdown')

    
def run_bot():
    bot_polling()
        

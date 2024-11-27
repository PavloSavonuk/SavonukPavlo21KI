import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import instructions, links


bot = telebot.TeleBot("7722883560:AAGmWsZc87t6UM6X6vjjodJNShy85s1Mj9Q")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я телеграм-бот, який допоможе тобі дізнатися про функції в Python.")
    bot.send_message(message.chat.id, "Список функцій про які я можу розповісти:")

    keyboard = InlineKeyboardMarkup(row_width=3)
    button = [InlineKeyboardButton(function.capitalize(), callback_data=function) for function in instructions.keys()]
    keyboard.add(*button)

    bot.send_message(message.chat.id, "Виберіть функцію:", reply_markup=keyboard)


@bot.callback_query_handler()
def function_info(call):
    function_name = call.data.lower()
    info = instructions.get(function_name)
    if info:
        bot.send_message(call.message.chat.id, info)
        link = links.get(function_name)
        if link:
            bot.send_message(call.message.chat.id, "Перейшовши за цим посиланням, ти можеш детальніше дізнатися про потрібну тобі функцію:")
            bot.send_message(call.message.chat.id, link)


bot.polling()

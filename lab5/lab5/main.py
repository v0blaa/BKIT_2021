import os
import telebot
from telebot import types

# Токент бота
TOKEN = '5037208404:AAFYv0F4BkExrzcoF7gwoBrnerJ69YMR3bY'

# Создание бота
bot = telebot.TeleBot(TOKEN)


# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    # bot.send_message(message.from_user.id, "Здравствуйте!\nЗачтите, пожалуйста, лабу 👉🏻👈🏻")
    # bot.register_next_step_handler(message, func(message))
    # bot.send_message(message.from_user.id, "я вышел из функции")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton("Хорошо, зачту")
    itembtn2 = types.KeyboardButton("Ладно, зачту")
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Здравствуйте!\nЗачтите, пожалуйста, лабу 👉🏻👈🏻", reply_markup=markup)
    if text == "Хорошо, зачту":
        bot.send_message(message.from_user.id, "Ура!!! Классно")
    elif text == "Ладно, зачту":
        bot.send_message(message.from_user.id, "Ура!!! Прикольно то как")
    elif text == "/help":
        bot.send_message(message.from_user.id, "Нажмите на кнопку")
    else:
        bot.send_message(message.from_user.id, "Я Вас не понимаю( Напишите /help.")

    # markup = types.ReplyKeyboardMarkup(row_width=2)
    # res = types.KeyboardButton("Увидимся на пересдаче!")
    # markup.add(res)
    # bot.send_message(message.chat.id, 'До свидания(((', reply_markup=markup)
    # bot.stop_bot()

# @bot.message_handler(content_types=['text'])
# def func(message):
#     bot.send_message(message.from_user.id, "я зашёл в функцию")
#     answer = message.text
#     while not answer:
#         answer = message.text
#     if answer == "Да":
#         bot.send_message(message.from_user.id, "Ура!!!")
#     elif answer == "Нет":
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         itembtn1 = types.KeyboardButton("Да")
#         itembtn2 = types.KeyboardButton("Да")
#         markup.add(itembtn1, itembtn2)
#         bot.send_message(message.chat.id, 'Кхм-кхм... Ещё раз...\nВы зачтёте мою лабораторную?', reply_markup=markup)
#
#     elif answer == "/help":
#         bot.send_message(message.from_user.id, "Напишите Да или Нет")
#     else:
#         bot.send_message(message.from_user.id, "Я Вас не понимаю. Напишите /help.")


bot.polling(none_stop=True, interval=0)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     # Идентификатор диалога
#     chat_id = message.chat.id
#
#     # Текст, введенный пользователем, то есть текст с кнопки
#     text = message.text
#
#     # Проверка сообщения и вывод данных
#     if text == mes_emblem:
#         img = open(os.path.join(cur_path, 'img\emblem.jpg'), 'rb')
#         bot.send_photo(chat_id, img)
#     elif text == mes_photo:
#         img = open(os.path.join(cur_path, 'img\photo.jpg'), 'rb')
#         bot.send_photo(chat_id, img)
#     else:
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         itembtn1 = types.KeyboardButton(mes_emblem)
#         itembtn2 = types.KeyboardButton(mes_photo)
#         markup.add(itembtn1, itembtn2)
#         bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)


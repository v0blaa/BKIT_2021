import os
import telebot
from telebot import types

# Токент бота
TOKEN = '5037208404:AAFYv0F4BkExrzcoF7gwoBrnerJ69YMR3bY'

# Создание бота
bot = telebot.TeleBot(TOKEN)

cat = "Котики"
dog = "Собачки"
bird = "Птички"
# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    chat_id = message.chat.id

    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text

    # Проверка сообщения и вывод данных
    if text == cat:
        img = open(os.path.join(cur_path, 'cat.png'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == dog:
        img = open(os.path.join(cur_path, 'dog.png'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == bird:
        img = open(os.path.join(cur_path, 'bird.png'), 'rb')
        bot.send_photo(chat_id, img)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=3)
        itembtn1 = types.KeyboardButton(cat)
        itembtn2 = types.KeyboardButton(dog)
        itembtn3 = types.KeyboardButton(bird)
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(chat_id, 'Здравствуйте! Нажмите любую кнопку внизу', reply_markup=markup)


bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    bot.infinity_polling()
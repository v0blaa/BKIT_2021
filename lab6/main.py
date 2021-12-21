import os
import telebot
from telebot import types
import random

# Токент бота
TOKEN = '5095553179:AAHkhDObVrZH7LWnnZ9x10yMny35xc_y1g8'

# Создание бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в наше заведение!')
    markup_inline = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Согласиться', callback_data="Agree")
    button_no = types.InlineKeyboardButton(text='Отказаться', callback_data="Disagree")
    markup_inline.add(button_yes, button_no)
    bot.send_message(message.chat.id, 'Сыграете в блэкджек?', reply_markup=markup_inline)

# @bot.message_handler(text="Agree")
# async def starting_game(call: types.CallbackQuery):
#     await call.message.answer(str(random.randint(2, 11)))

@bot.callback_query_handler(func=lambda c: c.data == 'Agree')
def start_game(callback_query: types.CallbackQuery):
    # bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ваши карты:')
    cards = cards_draw()
    new_card = cards_draw()
    cards[int(str(new_card)[1])] = new_card[int(str(new_card)[1])]

def cards_draw():
    card = {random.randint(1, 4): random.randint(2, 13)}
    #список мастей и список карт
    return card

@bot.callback_query_handler(func=lambda c: c.data == 'Disagree')
def exit_game(callback_query: types.CallbackQuery):
    bot.send_message(callback_query.from_user.id, 'До свидания!\nБудем рады видеть Вас снова')
    bot.stop_polling()


# def game(message):
#     markup_inline = types.InlineKeyboardMarkup()
#     button_more = types.InlineKeyboardButton(text='Ещё', callback_data="More")
#     button_enough = types.InlineKeyboardButton(text='Хватит', callback_data="Enough")
#     markup_inline.add(button_yes, button_no)
#     bot.send_message(message.chat.id, 'Ещё?', reply_markup=markup_inline)
# # По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
# @bot.message_handler(commands=['reset'])
# def cmd_reset(message):
#     bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
#     dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
#     bot.send_message(message.chat.id, 'Введите первое число')
#
#
# # Обработка первого числа
# @bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_FIRST_NUM.value)
# def first_num(message):
#     text = message.text
#     if not text.isdigit():
#         # Состояние не изменяется, выводится сообщение об ошибке
#         bot.send_message(message.chat.id, 'Пожалуйста введите число!')
#         return
#     else:
#         bot.send_message(message.chat.id, f'Вы ввели первое число {text}')
#         # Меняем текущее состояние
#         dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
#         # Сохраняем первое число
#         dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value), text)
#         bot.send_message(message.chat.id, 'Введите второе число')
#
#
# # Обработка второго числа
# @bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SECOND_NUM.value)
# def second_num(message):
#     text = message.text
#     if not text.isdigit():
#         # Состояние не изменяется, выводится сообщение об ошибке
#         bot.send_message(message.chat.id, 'Пожалуйста введите число!')
#         return
#     else:
#         bot.send_message(message.chat.id, f'Вы ввели второе число {text}')
#         # Меняем текущее состояние
#         dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
#         # Сохраняем первое число
#         dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value), text)
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         itembtn1 = types.KeyboardButton('+')
#         itembtn2 = types.KeyboardButton('*')
#         markup.add(itembtn1, itembtn2)
#         bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)
#
#
# # Выбор действия
# @bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
# def operation(message):
#     # Текущее действие
#     op = message.text
#     # Читаем операнды из базы данных
#     v1 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value))
#     v2 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value))
#     # Выполняем действие
#     fv1 = float(v1)
#     fv2 = float(v2)
#     res = 0
#     if op=='+':
#         res = fv1 + fv2
#     elif op=='*':
#         res = fv1 * fv2
#     # Выводим результат
#     markup = types.ReplyKeyboardRemove(selective=False)
#     bot.send_message(message.chat.id, f'Результат: {v1}{op}{v2}={str(res)}', reply_markup=markup)
#     # Меняем текущее состояние
#     dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
#     # Выводим сообщение
#     bot.send_message(message.chat.id, 'Введите первое число')


if __name__ == '__main__':
    bot.infinity_polling()
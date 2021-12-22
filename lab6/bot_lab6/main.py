import os
import telebot
from telebot import types
from game import Game
import random

# Токент бота
TOKEN = '5095553179:AAHkhDObVrZH7LWnnZ9x10yMny35xc_y1g8'

# Создание бота
bot = telebot.TeleBot(TOKEN)

game = None

cur_path = os.path.dirname(os.path.abspath(__file__))

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в наше заведение!')
    markup_inline = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Согласиться', callback_data="Agree")
    button_no = types.InlineKeyboardButton(text='Отказаться', callback_data="Disagree")
    markup_inline.add(button_yes, button_no)
    bot.send_message(message.chat.id, 'Сыграете в блэкджек?', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda c: c.data == 'Agree')
def handle_agree(callback_query: types.CallbackQuery):
    global game
    if game is not None:
        bot.send_message(callback_query.from_user.id, 'Игра уже начата')
        return
    game = Game()

    bot.send_message(callback_query.from_user.id, 'Ваши карты:' + "\n" + game.client.print_cards())
    bot.send_message(callback_query.from_user.id, "Очки: " + str(game.client.sum()))
    winner = check_finish()
    if winner is not None:
        congratulation_message(callback_query, winner)
        return

    bot.send_message(callback_query.from_user.id, 'Карта бота:' + "\n" + game.bot.print_cards(first_card=True))
    # bot.send_message(callback_query.from_user.id,  "Bot " + str(game.bot.sum()))
    winner = check_finish()
    if winner is not None:
        congratulation_message(callback_query, winner)
        return

    else:
        markup_inline = send_question()
        bot.send_message(callback_query.from_user.id, 'Еще?)', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda c: c.data == 'Disagree')
def handle_disagree(callback_query: types.CallbackQuery):
    finish(callback_query)

@bot.callback_query_handler(func=lambda c: c.data == 'No')
def handle_no(callback_query: types.CallbackQuery):
    if game is None:
        return
    winner = check_finish()

    if winner is None:
        if game.bot.sum() > game.client.sum():
            message = 'Победитель бот :('
        elif game.bot.sum() < game.client.sum():
            message = 'Вы победитель :)'
        elif game.bot.sum() == game.client.sum():
            message = 'Ничья :|'
        bot.send_message(callback_query.from_user.id, message)
        open_the_cards(callback_query)
        finish(callback_query)
        return
    congratulation_message(callback_query, check_finish())
    return

@bot.callback_query_handler(func=lambda c: c.data == 'Yes')
def handle_yes(callback_query: types.CallbackQuery):
    if five_cards(callback_query): return

    add_cards_to_client()
    bot.send_message(callback_query.from_user.id, 'Ваши карты:' + "\n" + game.client.print_cards())
    bot.send_message(callback_query.from_user.id, "Очки: " + str(game.client.sum()))
    winner = check_finish()
    if winner is not None:
        congratulation_message(callback_query, winner)
        return

    add_cards_to_bot()
    # bot.send_message(callback_query.from_user.id,  "Bot " + str(game.bot.sum()))
    winner = check_finish()
    if winner is not None:
        congratulation_message(callback_query, winner)
        return

    markup_inline = send_question()
    bot.send_message(callback_query.from_user.id, 'Еще?)', reply_markup=markup_inline)

def send_question():
    markup_inline = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data="Yes")
    button_no = types.InlineKeyboardButton(text='Нет', callback_data="No")
    markup_inline.add(button_yes, button_no)
    return markup_inline

# доделать
def check_finish():
    bot_sum = game.bot.sum()
    client_sum = game.client.sum()

    if client_sum == 21:
        return 'client'
    elif bot_sum > 21:
        return 'client'
    elif bot_sum == 21:
        return 'bot'
    elif client_sum > 21:
        return 'bot'

    return None


def add_cards_to_client():
    game.add_new_cards_to_client()

def add_cards_to_bot():
    game.add_new_cards_to_bot()

def five_cards(callback_query):
    if game.client.count_cards() >= 5:
        bot.send_message(callback_query.from_user.id, 'У Вас 5 карт! Вскрываемся!')
        congratulation_message(callback_query, check_finish())
        return True

def congratulation_message(callback_query, winner):
    bot.send_message(callback_query.from_user.id, 'Победитель ' + winner + ' !')
    open_the_cards(callback_query)
    finish(callback_query)
    return

def open_the_cards(callback_query):
    bot.send_message(callback_query.from_user.id, '___________________________')
    bot.send_message(callback_query.from_user.id, '\nИТОГИ:\n')
    bot.send_message(callback_query.from_user.id, 'Ваши карты:' + "\n" + game.client.print_cards())
    bot.send_message(callback_query.from_user.id, "Очки: " + str(game.client.sum()))
    bot.send_message(callback_query.from_user.id, '\nКарты бота:' + "\n" + game.bot.print_cards())
    bot.send_message(callback_query.from_user.id, "Очки: " + str(game.bot.sum()))
    bot.send_message(callback_query.from_user.id, '___________________________')

def finish(callback_query):
    global game
    game = None
    bot.send_message(callback_query.from_user.id, 'До свидания!\nБудем рады видеть Вас снова')

if __name__ == '__main__':
    bot.infinity_polling()
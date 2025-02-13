import telebot
import requests
import json
import webbrowser
from telebot import types
bot = telebot.TeleBot('7578450317:AAEgfZQqXITlxBMEi71pnYnVSvkuBGK9KD0')
# создаем кнопки и добавляем их
@bot.message_handler(commands=['site'])
def start_message(message):
    mm = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('мой сайт', url='https://habr.com/ru/all/')
    btn2 = types.InlineKeyboardButton('удалить сообщение', callback_data='delete')
    mm.add(btn1, btn2)
    bot.send_message(message.chat.id, 'привет, зайди на мой сайт', reply_markup=mm)

# делаем чтобы при нажатии на кнопку сообщение удалялось
@bot.callback_query_handler(func= lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.answer_callback_query(callback.id)

# делаем чтобы бот при написании 'привет' бот отправлял стикер и сообщение

@bot.message_handler(content_types=['text'])
def message_text(message):
    if message.text == 'привет':
        sti = open('Sticker.tgs' , 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '<b>привет!</b> надеюсь тебе понравится бот!', parse_mode='html')


bot.polling(none_stop=True)

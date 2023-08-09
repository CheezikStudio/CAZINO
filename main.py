#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
import random
def main():
    while True:
        if True:
            bot = telebot.TeleBot('6495412157:AAFqBSlboEieZmc3E_hVr81rXfOBUVRreks')
            @bot.message_handler(commands=["start", "admin"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("CAZINO.db")
                c  = db.cursor()
                if message.text == "/admin":
                    pass
                if message.text == "/start":
                    c.execute("""SELECT number FROM users WHERE idtg= ?""", [idtg])
                    if c.fetchone() == None:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Дать свой номер", request_contact=True)
                        markup.add(btn1)
                        file = open("hello.jpg", "rb")
                        bot.send_photo(idtg, file, f''' Добро пожаловать в нашего игрового бота!В этом боте вы можете играть в различные интересные игры. \n <b>Для начала нужно дать свой номер, чтобы автоматический вывод работал корректно!</b> ''',reply_markup=markup,parse_mode='HTML')
                    else:
                        c.execute("""SELECT allvivod FROM static """)
                        Alltake= c.fetchone()
                        c.execute("""SELECT allzarabotano FROM static """)
                        Allprofit= c.fetchone()
                        c.execute("""SELECT allusers FROM static """)
                        Allplayers= c.fetchone()
                        c.execute("""SELECT lastdep FROM static """)
                        Lastdeposit= c.fetchone()
                        bot.delete_message(idtg, message.message_id)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardMarkup(text="Меню игр📜", callback_data=f"playmenu")
                        btn2 = types.InlineKeyboardMarkup(text="Профиль", callback_data=f"profile")
                        btn3 = types.InlineKeyboardMarkup(text="Пополнить", callback_data=f"deposit")
                        btn4 = types.InlineKeyboardMarkup(text="Вывести", callback_data=f"take")
                        btn5 = types.InlineKeyboardMarkup(text="Книга Отзывов📕", callback_data=f"callback")
                        btn6 = types.InlineKeyboardMarkup(text="Связь с администацией", callback_data=f"messageadm")
                        markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
                        file = open("glav.jpg", "rb")
                        bot.send_photo(message.chat.id, file, f'''
 Статистика бота:\nВсего выведено:{Alltake}\nЗаработано:{Allprofit}\nВсего игроков:{Allplayers}\nПоследний вывод:{Lastdeposit}

                        ''',  reply_markup=markup, parse_mode='HTML')
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                global perexod
                perexod = " "
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("CAZINO.db")
                c = db.cursor()
                if call.data == "glavmenu":
                    c.execute("""SELECT number FROM users WHERE idtg= ?""", [idtg])
                    if c.fetchone() == None:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Дать свой номер", request_contact=True)
                        markup.add(btn1)
                        file = open("hello.jpg", "rb")
                        bot.send_photo(idtg, file, f''' Добро пожаловать в нашего игрового бота!В этом боте вы можете играть в различные интересные игры. \n <b>Для начала нужно дать свой номер, чтобы автоматический вывод работал корректно!</b> ''',reply_markup=markup,parse_mode='HTML')
                    else:
                        c.execute("""SELECT allvivod FROM static """)
                        Alltake= c.fetchone()
                        c.execute("""SELECT allzarabotano FROM static """)
                        Allprofit= c.fetchone()
                        c.execute("""SELECT allusers FROM static """)
                        Allplayers= c.fetchone()
                        c.execute("""SELECT lastdep FROM static """)
                        Lastdeposit= c.fetchone()
                        bot.delete_message(idtg, call.message.message_id)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardMarkup(text="Меню игр📜", callback_data=f"playmenu")
                        btn2 = types.InlineKeyboardMarkup(text="Профиль", callback_data=f"profile")
                        btn3 = types.InlineKeyboardMarkup(text="Пополнить", callback_data=f"deposit")
                        btn4 = types.InlineKeyboardMarkup(text="Вывести", callback_data=f"take")
                        btn5 = types.InlineKeyboardMarkup(text="Книга Отзывов📕", callback_data=f"callback")
                        btn6 = types.InlineKeyboardMarkup(text="Связь с администацией", callback_data=f"messageadm")
                        markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
                        file = open("glav.jpg", "rb")
                        bot.send_photo(idtg, file, f'''
Статистика бота:\nВсего выведено:{Alltake}\nЗаработано:{Allprofit}\nВсего игроков:{Allplayers}\nПоследний вывод:{Lastdeposit}

                        ''',  reply_markup=markup, parse_mode='HTML')
                if call.data == "take":
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardMarkup(text="Qiwi(Автоматический перевод)", callback_data=f"Qiwi")
                    btn2 = types.InlineKeyboardMarkup(text="Сбер(Полуавтоматический перевод)", callback_data=f"Sber")
                    markup.add(btn1, btn2)
                    file = open("dev.jpg", "rb")
                    bot.send_photo(idtg, file, f'''
Выбери способ вывода:
                        ''',  reply_markup=markup, parse_mode='HTML')
                if call.data == "deposit":
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardMarkup(text="Qiwi(Автоматический перевод)", callback_data=f"Qiwi")
                    btn2 = types.InlineKeyboardMarkup(text="Сбер(Полуавтоматический перевод)", callback_data=f"Sber")
                    btn3 = types.InlineKeyboardMarkup(text="Юмоней(Автоматический перевод)", callback_data=f"Umoney")
                    markup.add(btn1, btn2, btn3)
                    file = open("dev.jpg", "rb")
                    bot.send_photo(idtg, file, f'''
Выбери способ вывода:
                        ''',  reply_markup=markup, parse_mode='HTML')
                if call.data == "callback":
                    bot.delete_message(idtg, call.message.message_id)
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Наши отзывы😎", callback_data=f"otziv")
                    btn2 = types.InlineKeyboardButton(text="Написать пожелание🙏", callback_data=f"pozhelanie")
                    btn3 = types.InlineKeyboardButton(text="Вернутся в главное меню👈", callback_data=f"glavmenu")
                    markup.add(btn1, btn2, btn3)
                    file = open("Otziv.jpg", "rb")
                    bot.send_photo(call.message.chat.id, file, f'''
<b>Книга Отзывов📕</b>
Здесь вы можете посмотреть на отзывы наших игроков
Также написать своё пожелание/отзыв для нашего бота!
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "otziv" in call.data:
                    bot.delete_message(idtg, call.message.message_id)
                    x = int(call.data.split(" ")[1])
                    markup = types.InlineKeyboardMarkup(row_width = 2)
                    c.execute("""SELECT * FROM reviews WHERE rowid = ?""", [x])
                    data = c.fetchone()
                    try:
                        c.execute("""SELECT Totalvivod FROM profile WHERE idtg = ?""", [data[0]])
                        ord = len(c.fetchall())
                    except:
                        ord = "0"
                    c.execute("""SELECT * FROM reviews""")
                    count = len(c.fetchall())
                    if x == 1:
                        btn1 = types.InlineKeyboardButton(text="⏪", callback_data=f"otziv {count}")
                    else:
                        btn1 = types.InlineKeyboardButton(text="⏪", callback_data=f"otziv {int(x)-1}")
                    if x == count:
                        btn2 = types.InlineKeyboardButton(text="⏩", callback_data=f"otziv {1}")
                    else:
                        btn2 = types.InlineKeyboardButton(text="⏩", callback_data=f"otziv {int(x)+1}")
                    btn3 = types.InlineKeyboardButton(text="Вернуться к пожеланиям👈", callback_data=f"callback")
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(call.message.chat.id, f'''
<b>Имя - {data[1]}</b>
Выводов в боте - {ord}
Отзыв:
<b>{data[2]}</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                if call.data == "pozhelanie":
                    bot.delete_message(idtg, call.message.message_id)
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Я передумал🙊")
                    markup.add(btn1)
                    bot.send_message(call.message.chat.id, f'''
<i>Этап 1/2</i>
<b>Напишите своё имя:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    perexod = "callback"
            @bot.message_handler(content_types=['text'])
            def menu(message):
                global perexod
                idtg = str(message.from_user.id)
                db = sqlite3.connect("CAZINO.db")
                c  = db.cursor()
                if perexod == "callback":
                    if message.text == "Я передумал🙊":
                        perexod = " "
                        print(perexod, 32423)
                        bot.delete_message(idtg, message.message_id)
                        bot.delete_message(idtg, int(message.message_id)-1)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Наши отзывы😎", callback_data=f"otziv")
                        btn2 = types.InlineKeyboardButton(text="Написать пожелание🙏", callback_data=f"pozhelanie")
                        btn3 = types.InlineKeyboardButton(text="Вернутся в главное меню👈", callback_data=f"glavmenu")
                        markup.add(btn1, btn2, btn3)
                        file = open("Otziv.jpg", "rb")
                        bot.send_photo(message.chat.id, file, f'''
<b>Книга Отзывов📕</b>
Здесь вы можете посмотреть на отзывы наших игроков
Также написать своё пожелание/отзыв для нашего бота!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    else:
                        name = message.text
                        bot.delete_message(idtg, message.message_id)
                        bot.delete_message(idtg, int(message.message_id)-1)
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Я передумал🙊")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
    <i>Этап 2/2</i>
    <b>Напишите пожелание/отзыв:</b>

                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, otziv, name)
                else:
                    c.execute("""SELECT number FROM users WHERE idtg= ?""", [idtg])
                    if c.fetchone() == None:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Дать свой номер", request_contact=True)
                        markup.add(btn1)
                        file = open("hello.jpg", "rb")
                        bot.send_photo(idtg, file, f''' Добро пожаловать в нашего игрового бота!В этом боте вы можете играть в различные интересные игры. \n <b>Для начала нужно дать свой номер, чтобы автоматический вывод работал корректно!</b> ''',reply_markup=markup,parse_mode='HTML')
                    else:
                        c.execute("""SELECT allvivod FROM static """)
                        Alltake= c.fetchone()
                        c.execute("""SELECT allzarabotano FROM static """)
                        Allprofit= c.fetchone()
                        c.execute("""SELECT allusers FROM static """)
                        Allplayers= c.fetchone()
                        c.execute("""SELECT lastdep FROM static """)
                        Lastdeposit= c.fetchone()
                        bot.delete_message(idtg, message.message_id)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardMarkup(text="Меню игр📜", callback_data=f"playmenu")
                        btn2 = types.InlineKeyboardMarkup(text="Профиль", callback_data=f"profile")
                        btn3 = types.InlineKeyboardMarkup(text="Пополнить", callback_data=f"deposit")
                        btn4 = types.InlineKeyboardMarkup(text="Вывести", callback_data=f"take")
                        btn5 = types.InlineKeyboardMarkup(text="Книга Отзывов📕", callback_data=f"callback")
                        btn6 = types.InlineKeyboardMarkup(text="Связь с администацией", callback_data=f"messageadm")
                        markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
                        file = open("glav.jpg", "rb")
                        bot.send_photo(message.chat.id, file, f'''
 Статистика бота:\nВсего выведено:{Alltake}\nЗаработано:{Allprofit}\nВсего игроков:{Allplayers}\nПоследний вывод:{Lastdeposit}

                        ''',  reply_markup=markup, parse_mode='HTML')
                        perexod = " "
                def otziv(message, name):
                    db = sqlite3.connect("CAZINO.db")
                    c  = db.cursor()
                    idtg = str(message.from_user.id)
                    otzivtext = message.text
                    if message.text == "Я передумал🙊":
                        bot.delete_message(idtg, message.message_id)
                        bot.delete_message(idtg, int(message.message_id)-1)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Наши отзывы😎", callback_data=f"otziv")
                        btn2 = types.InlineKeyboardButton(text="Написать пожелание🙏", callback_data=f"pozhelanie")
                        btn3 = types.InlineKeyboardButton(text="Вернутся в главное меню👈", callback_data=f"glavmenu")
                        markup.add(btn1, btn2, btn3)
                        perexod = " "
                        file = open("Otziv.jpg", "rb")
                        bot.send_photo(message.chat.id, file, f'''
<b>Книга Отзывов📕</b>
Здесь вы можете посмотреть на отзывы наших игроков
Также написать своё пожелание/отзыв для нашего бота!
                        ''',  reply_markup=markup, parse_mode='HTML')
                    else:
                        bot.delete_message(idtg, message.message_id)
                        bot.delete_message(idtg, int(message.message_id)-1)
                        c.execute(f"INSERT INTO reviews VALUES (?,?,?)",(idtg, name, message.text))
                        db.commit()
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Вернуться к книге📕", callback_data=f"callback")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
    Ваш отзыв записан! Спасибо, вы делаете нас лучше!💌
                        ''',  reply_markup=markup, parse_mode='HTML')
                    perexod = " "
            bot.message_handler(content_types=['contact'])
            def contact(message):
                if message.contact is not None:
                    idtg = str(message.from_user.id)
                    db = sqlite3.connect("bakery.db")
                    c  = db.cursor()
                    bot.send_message(message.chat.id, '_', reply_markup=types.ReplyKeyboardRemove())
                    bot.delete_message(idtg, message.message_id-1)
                    bot.delete_message(idtg, message.message_id)
                    bot.delete_message(idtg, message.message_id+1)
                    markup = types.InlineKeyboardMarkup(row_width = 2)
                    btn1 = types.InlineKeyboardButton(text="Перейти в главное меню", callback_data=f"glavmenu")
                    markup.add(btn1)
                    global phonenumber
                    phonenumber= str(message.contact.phone_number)
                    c.execute(f"INSERT INTO users VALUES (?,?,?)",(idtg, phonenumber,0))
                    db.commit()
                    bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=markup)


































            bot.infinity_polling()
        else:
            pass
main()

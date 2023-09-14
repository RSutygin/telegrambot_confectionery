import telebot
from telebot import types
import os
from dotenv import load_dotenv
import requests_sql
from connect_db import connect_to_database

load_dotenv('config.env')

token = os.getenv('TOKEN')
my_id = os.getenv('MY_ID')


class Bot:
    def __init__(self):
        self.conn = connect_to_database()  # connecting to the database

        self.keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_cupcakes = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_trifles = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_bento_1kg = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_bento_05kg = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_tort = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_count = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_weight_bento = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_weight_tort = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_decor = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_messenger = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_yes_or_no = types.ReplyKeyboardMarkup(resize_keyboard=True)  # all keyboards

        item_main = types.KeyboardButton("Главное меню")
        item_decor = types.KeyboardButton("Обсуждение декора")
        item_more = types.KeyboardButton("Больше или меньше")

        # item81 = types.KeyboardButton("Курс - Сам себе кондитер")

        item_cupcakes = types.KeyboardButton("Капкейки")
        item_trifles = types.KeyboardButton("Трайфлы")
        item_bento = types.KeyboardButton("Бенто-торт")
        item_cakes = types.KeyboardButton("Торты")

        item_count_6 = types.KeyboardButton("6")
        item_count_9 = types.KeyboardButton("9")
        item_count_12 = types.KeyboardButton("12")

        item_bento_s = types.KeyboardButton("Сникерс")
        item_bento_kb = types.KeyboardButton("Красный бархат")
        item_bento_bc = types.KeyboardButton("Blue cake")
        item_bento_tc = types.KeyboardButton("Toffifee cake")
        item_bento_pk = types.KeyboardButton("Пряная карамель")

        item_bento05_y = types.KeyboardButton("Йогуртовый")
        item_bento05_k = types.KeyboardButton("Клубничный")

        item_bento_weight_05 = types.KeyboardButton("Стандартный")
        item_bento_weight_1 = types.KeyboardButton("1 кг")

        item_cake_kb = types.KeyboardButton("Красный бархат")
        item_cake_bc = types.KeyboardButton("Blue cake")
        item_cake_ks = types.KeyboardButton("Кофе со сливками")
        item_cake_kk = types.KeyboardButton("Клубничный каприз")
        item_cake_oc = types.KeyboardButton("Орео кейк")
        item_cake_pk = types.KeyboardButton("Пряная карамель")
        item_cake_r = types.KeyboardButton("Рафаэлло")
        item_cake_s = types.KeyboardButton("Сникерс")
        item_cake_tc = types.KeyboardButton("Toffifee cake")

        item_cake_weight_15 = types.KeyboardButton('1,5 кг')
        item_cake_weight_2 = types.KeyboardButton('2 кг')
        item52_cake_weight_25 = types.KeyboardButton('2,5 кг')
        item_cake_weight_3 = types.KeyboardButton('3 кг')
        item_cake_weight_35 = types.KeyboardButton('3,5 кг')
        item_cake_weight_4 = types.KeyboardButton('4 кг')

        item_cupcake_y = types.KeyboardButton("Йогуртовые")
        item_cupcake_m = types.KeyboardButton("Морковные")
        item_cupcake_kb = types.KeyboardButton("Красный бархат")
        item_cupcake_s = types.KeyboardButton("Сникерс")

        item_trifle_y = types.KeyboardButton("Йогуртовые")
        item_trifle_kb = types.KeyboardButton("Красный бархат")
        item4_trifle_s = types.KeyboardButton("Сникерс ")

        item_messenger_wa = types.KeyboardButton("WhatsApp")
        item_messenger_i = types.KeyboardButton("Instagram")
        item_messenger_t = types.KeyboardButton("Telegram")

        item_yes = types.KeyboardButton("Да")
        item_no = types.KeyboardButton("Нет")  # all keyboards buttons

        self.keyboard_main.add(item_cupcakes, item_trifles, item_bento, item_cakes)
        self.keyboard_count.add(item_count_6, item_count_9, item_count_12, item_more, item_main)
        self.keyboard_bento_1kg.add(item_bento_s, item_bento_kb, item_bento_bc, item_bento_tc, item_bento_pk, item_main)
        self.keyboard_tort.add(item_cake_kb, item_cake_bc, item_cake_ks, item_cake_kk, item_cake_oc, item_cake_pk,
                               item_cake_r, item_cake_s, item_cake_tc, item_main)
        self.keyboard_cupcakes.add(item_cupcake_y, item_cupcake_m, item_cupcake_kb, item_cupcake_s, item_main)
        self.keyboard_trifles.add(item_trifle_y, item_trifle_kb, item4_trifle_s, item_main)
        self.keyboard_weight_bento.add(item_bento_weight_05, item_bento_weight_1, item_main)
        self.keyboard_weight_tort.add(item_cake_weight_15, item_cake_weight_2, item52_cake_weight_25,
                                      item_cake_weight_3, item_cake_weight_35, item_cake_weight_4, item_more, item_main)
        self.keyboard_decor.add(item_decor, item_main)
        self.keyboard_messenger.add(item_messenger_wa, item_messenger_i, item_messenger_t, item_main)
        self.keyboard_bento_05kg.add(item_bento05_y, item_bento05_k, item_main)
        self.keyboard_yes_or_no.add(item_yes, item_no, item_main)

        self.bot = telebot.TeleBot(token)

        @self.bot.message_handler(commands=['start'])
        def start(message):  # receiving message "/start"
            self.bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Елена Сутыгина, Я домашний кондитер!\n'
                                                   'Используйте кнопки выбора, предлагаемые ботом, если будет '
                                                   'необходимость '
                                                   'ввести что то с клавиатуры, бот Вас об этом попросит.\n'
                                                   'Если кнопок нет, а есть только клавиатура, справа от окошка, '
                                                   'где набирается '
                                                   'текст, нажмите на кнопку с 4 точками.',
                                  reply_markup=self.keyboard_main)  # sending greetings

            if self.conn:  # checking if the connection exists
                if requests_sql.add_id(self.conn, message.chat.id):  # if there is no name in the database, ask him
                    self.bot.send_message(message.chat.id, 'Введите Ваше имя:',
                                          reply_markup=types.ReplyKeyboardRemove())
                    self.bot.register_next_step_handler(message, self.name)  # in which method of the class to wait
                    # for the next message

                else:  # else welcome by name
                    name = requests_sql.get_name(self.conn, message.chat.id)  # get name
                    self.bot.send_message(message.chat.id, f'{name[0][0]}, с возвращением!',
                                          reply_markup=types.ReplyKeyboardRemove())  # sending greetings
                    self.bot.send_message(message.chat.id, 'Выберите интересующий Вас десерт:',
                                          reply_markup=self.keyboard_main)
                    self.bot.register_next_step_handler(message, self.main_menu)  # in which method of the class to wait
                    # for the next message

            else:  # if the connection does not exist
                self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to the main menu

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):  # receiving message with any text
            if self.conn:  # checking if the connection exists

                name = requests_sql.get_name(self.conn, message.chat.id)  # get name

                if name:  # if the name exists in the database
                    self.bot.send_message(message.chat.id, f'{name[0][0]}, с возвращением!',
                                          reply_markup=types.ReplyKeyboardRemove())  # sending greetings with name
                    self.bot.send_message(message.chat.id, 'Выберите интересующий Вас десерт:',
                                          reply_markup=self.keyboard_main)
                    self.bot.register_next_step_handler(message, self.main_menu)  # in which method of the class to wait
                    # for the next message

                else:  # if no name in the database, send a start message
                    start(message)

            else:  # if the connection does not exist
                self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to the main menu

        @self.bot.message_handler(content_types=['photo'])
        def photo(message):  # if user sent a photo
            if self.conn:  # checking if the connection exists
                file_id = message.photo[-1].file_id  # get file id
                file_info = self.bot.get_file(file_id)  # get file
                downloaded_file = self.bot.download_file(file_info.file_path)  # url for file

                i = 0  # counter
                while True:
                    if os.path.exists(f"{message.chat.id}_{i}.jpg"):  # if the file exists
                        i += 1  # counter +1
                    else:  # if the file not exists
                        break  # break cycle

                with open(f"{message.chat.id}_{i}.jpg", 'wb') as new_file:  # open a file for writing
                    new_file.write(downloaded_file)

                requests_sql.update_decor(self.conn, message.chat.id, f'Фото {message.chat.id}_{i}.jpg')  # write the
                # name of the file to the database

                self.check_photo(message)  # ask the user about a new file

            else:  # if the connection does not exist
                self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to the main menu

    def run_pooling(self):
        self.bot.polling(none_stop=True)

    def name(self, message):  # get name
        if self.conn:  # checking if the connection exists
            requests_sql.update_name(self.conn, message.chat.id, message.text)  # write name of user to the database
            self.bot.send_message(message.chat.id, f'Приятно познакомиться, {message.text}!')  # sending greetings
            self.bot.send_message(message.chat.id, 'Выберите интересующий Вас десерт:', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # in which method of the class to wait
            # for the next message

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)

    def main_menu(self, message):  # get a message from the main menu
        if message.text.strip() == 'Капкейки':  # if message text is 'Капкейки'
            self.bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/UVj7EvM8Q_cXtA')  # sending photo
            self.bot.send_message(message.chat.id, 'Выберите начинку капкейков:',
                                  reply_markup=self.keyboard_cupcakes)
            self.bot.register_next_step_handler(message, self.cupcake)  # in which method of the class to wait
            # for the next message

        elif message.text.strip() == 'Трайфлы':  # if message text is 'Трайфлы'
            self.bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/NKHKbkm8HhSTCQ')  # sending photo
            self.bot.send_message(message.chat.id, 'Выберите начинку трайфлов:', reply_markup=self.keyboard_trifles)
            self.bot.register_next_step_handler(message, self.trifles)  # in which method of the class to wait
            # for the next message

        elif message.text.strip() == 'Бенто-торт':  # if message text is 'Бенто-торт'
            self.bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/52j33QkBgYb_lA')  # sending photo
            self.bot.send_message(message.chat.id, 'Выберите вес бенто-торта:', reply_markup=self.keyboard_weight_bento)
            self.bot.register_next_step_handler(message, self.weight_bento)  # in which method of the class to wait
            # for the next message

        elif message.text.strip() == 'Торты':  # if message text is 'Торты'
            all_photo = [types.InputMediaPhoto('https://disk.yandex.ru/i/Cos-7DQfEMLOvw'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/N5A25pnh35TFOA'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/lbTaMsS5MkTweg'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/Tp5yklDTVzWx9w'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/BZel1vBBq7xT0g'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/ujOruUDQ-9339g'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/6DhC-5Dwd5JYVA'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/LDT6Ddd0Q66inQ'),
                         types.InputMediaPhoto('https://disk.yandex.ru/i/tZi2jcXZdp2THw')
                         ]  # group photo
            self.bot.send_media_group(message.chat.id, all_photo)  # sending group photo
            self.bot.send_message(message.chat.id, 'Выберите начинку торта:', reply_markup=self.keyboard_tort)
            self.bot.register_next_step_handler(message, self.cakes)  # in which method of the class to wait
            # for the next message

    def cupcake(self, message):   # get a message from the cupcakes menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Йогуртовые':  # if message text is 'Йогуртовые'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Йогуртовые капкейки')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество капкейков:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Морковные':  # if message text is 'Морковные'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Морковные капкейки')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество капкейков:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Красный бархат':  # if message text is 'Красный бархат'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Красный бархат капкейки')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество капкейков:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Сникерс':  # if message text is 'Сникерс'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Сникерс капкейки')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество капкейков:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def trifles(self, message):   # get a message from the trifles menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Йогуртовые':  # if message text is 'Йогуртовые'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Йогуртовые трайфлы')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество трайфлов:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Красный бархат':  # if message text is 'Красный бархат'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Красный бархат трайфлы')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество трайфлов:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Сникерс':  # if message text is 'Сникерс'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Сникерс трайфлы')  # write dessert
                # name of to the database
                self.bot.send_message(message.chat.id, 'Выберите количество трайфлов:',
                                      reply_markup=self.keyboard_count)
                self.bot.register_next_step_handler(message, self.count)  # in which method of the class to wait
            # for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def count(self, message):   # get a message from the count menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == '6':  # if message text is count dessert
                requests_sql.update_count(self.conn, message.chat.id, 6)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to wait
                # for the next message

            elif message.text.strip() == '9':  # if message text is count dessert
                requests_sql.update_count(self.conn, message.chat.id, 9)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to wait
                # for the next message

            elif message.text.strip() == '12':  # if message text is count dessert
                requests_sql.update_count(self.conn, message.chat.id, 12)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to wait
                # for the next message

            elif message.text.strip() == 'Больше или меньше':  # if message text is count dessert
                requests_sql.update_count(self.conn, message.chat.id, 99999999)  # write count dessert of to the
                # database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                self.bot.send_message(message.chat.id, f'Цена будет указана после обсуждения с Вами всех деталей. '
                                                       f'Перейти к обсуждению декора?',
                                      reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to wait
                # for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def weight_bento(self, message):   # get a message from the weight bento menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Стандартный':  # if message text is 'Стандартный'
                requests_sql.update_count(self.conn, message.chat.id, 0.5)  # write count dessert of to the
                # database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                self.bot.send_message(message.chat.id, f'Выберите начинку бенто-торта:',
                                      reply_markup=self.keyboard_bento_05kg)
                self.bot.register_next_step_handler(message, self.bento_cakes_05kg)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '1 кг':  # if message text is '1 кг'
                requests_sql.update_count(self.conn, message.chat.id, 1)  # write count dessert of to the
                # database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                self.bot.send_message(message.chat.id, f'Выберите начинку бенто-торта:',
                                      reply_markup=self.keyboard_bento_1kg)
                self.bot.register_next_step_handler(message, self.bento_cakes_1kg)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def bento_cakes_1kg(self, message):   # get a message from the bento cakes 1kg menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Сникерс':  # if message text is 'Сникерс'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Сникерс бенто 1кг')  # write dessert
                # name of to the database
                requests_sql.update_price(self.conn, message.chat.id)
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Красный бархат':  # if message text is 'Красный бархат'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Красный бархат бенто 1кг')  # write
                # dessert name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Blue cake':  # if message text is 'Blue cake'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Blue cake бенто 1кг')  # write dessert
                # name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Toffifee cake':  # if message text is 'Toffifee cake'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Toffifee cake бенто 1кг')  # write dessert
                # name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Пряная карамель':  # if message text is 'Пряная карамель'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Пряная карамель бенто 1кг')  # write
                # dessert name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def bento_cakes_05kg(self, message):   # get a message from the bento cakes 0.5kg menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Йогуртовый':  # if message text is 'Йогуртовый'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Йогуртовый бенто 0,5кг')  # write
                # dessert name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Клубничный':  # if message text is 'Клубничный'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Клубничный бенто 0,5кг')  # write
                # dessert name of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def cakes(self, message):   # get a message from the cakes menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Красный бархат':  # if message text is 'Красный бархат'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Красный бархат торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Blue cake':  # if message text is 'Blue cake'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Blue cake торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Кофе со сливками':  # if message text is 'Кофе со сливками'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Кофе со сливками торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Клубничный каприз':  # if message text is 'Клубничный каприз'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Клубничный каприз торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Орео кейк':  # if message text is 'Орео кейк'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Орео кейк торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Пряная карамель':  # if message text is 'Пряная карамель'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Пряная карамель торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Рафаэлло':  # if message text is 'Рафаэлло'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Рафаэлло торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Сникерс':  # if message text is 'Сникерс'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Сникерс торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Toffifee cake':  # if message text is 'Toffifee cake'
                requests_sql.update_dessert(self.conn, message.from_user.id, 'Toffifee cake торт')  # write
                # dessert name of to the database
                self.bot.send_message(message.chat.id, 'Выберите вес торта:', reply_markup=self.keyboard_weight_tort)
                self.bot.register_next_step_handler(message, self.weight_cake)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def weight_cake(self, message):   # get a message from the weight cakes menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == '1,5 кг':  # if message text is '1,5 кг'
                requests_sql.update_count(self.conn, message.chat.id, 1.5)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '2 кг':  # if message text is '2 кг'
                requests_sql.update_count(self.conn, message.chat.id, 2)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '2,5 кг':  # if message text is '2,5 кг'
                requests_sql.update_count(self.conn, message.chat.id, 2.5)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '3 кг':  # if message text is '3 кг'
                requests_sql.update_count(self.conn, message.chat.id, 3)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '3,5 кг':  # if message text is '3,5 кг'
                requests_sql.update_count(self.conn, message.chat.id, 3.5)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == '4 кг':  # if message text is '4 кг'
                requests_sql.update_count(self.conn, message.chat.id, 4)  # write count dessert of to the database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                price = requests_sql.get_price(self.conn, message.chat.id)  # get price if the database
                self.bot.send_message(message.chat.id, f'Цена без учета оформления: {int(price[0][0])} рублей, '
                                                       f'перейти к обсуждению '
                                                       f'декора?', reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Больше или меньше':  # if message text is 'Больше или меньше'
                requests_sql.update_count(self.conn, message.chat.id, 99999999)  # write count dessert of to the
                # database
                requests_sql.update_price(self.conn, message.chat.id)  # write price dessert of to the database
                self.bot.send_message(message.chat.id, f'Цена будет указана после обсуждения с Вами всех деталей. '
                                                       f'Перейти к обсуждению декора?',
                                      reply_markup=self.keyboard_decor)
                self.bot.register_next_step_handler(message, self.decor)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def decor(self, message):   # get a message from the decor menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Обсуждение декора':  # if message text is 'Обсуждение декора'
                self.bot.send_message(message.chat.id, 'У Вас есть фото примерного декора, который Вы хотите?',
                                      reply_markup=self.keyboard_yes_or_no)
                self.bot.register_next_step_handler(message, self.decor_yes_or_no)  # in which method of the class to
                # wait for the next message
            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def decor_yes_or_no(self, message):   # get a message from the yes or no menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Да':  # if message text is 'Да'
                self.bot.send_message(message.chat.id, 'Пришлите фото декора, который Вы хотите.\n'
                                                       'Если фото несколько, присылайте по одному, бот подскажет Вам,'
                                                       'когда нужно прислать следующее.',
                                      reply_markup=types.ReplyKeyboardRemove())

            elif message.text.strip() == 'Нет':  # if message text is 'Нет'
                self.bot.send_message(message.chat.id, 'Пожалуйста, напишите, на какое мероприятие Вы заказываете '
                                                       'десерт, укажите пол, возраст человека, которому '
                                                       'предназначается десерт, его интересы/хобби, любимого '
                                                       'персонажа и тому подобное, на основе данной информации Я '
                                                       'помогу Вам подобрать оформление:',
                                      reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.decor_text)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def decor_text(self, message):   # get a message from decor text
        if self.conn:  # checking if the connection exists
            if message.text.strip():  # if message text
                requests_sql.update_decor(self.conn, message.chat.id, message.text)  # write decor text in the database
                self.bot.send_message(message.chat.id, 'Введите дату, на которую Вы хотите сделать заказ:',
                                      reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.date)  # in which method of the class to
                # wait for the next message

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def check_photo(self, message):  # checking if there are more photos
        if self.conn:  # checking if the connection exists
            self.bot.send_message(message.chat.id, 'Хотите прислать еще одно фото?',
                                  reply_markup=self.keyboard_yes_or_no)
            self.bot.register_next_step_handler(message, self.check_photo_yes_or_no)  # in which method of the class to
            # wait for the next message

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def check_photo_yes_or_no(self, message):   # get a message from the yes or no menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Да':  # if message text is 'Да'
                self.bot.send_message(message.chat.id, 'Пришлите фото декора, который Вы хотите:',
                                      reply_markup=types.ReplyKeyboardRemove())
            elif message.text.strip() == 'Нет':  # if message text is 'Нет'
                self.bot.send_message(message.chat.id, 'Введите дату, на которую Вы хотите сделать заказ:',
                                      reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.date)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def date(self, message):   # get a message with date
        if self.conn:  # checking if the connection exists
            if message.text.strip():  # if message text
                requests_sql.update_date(self.conn, message.chat.id, message.text)  # write date of to the database
                if not requests_sql.check_messenger_and_number(self.conn, message.chat.id):  # if not messenger name
                    # and phone/username
                    self.bot.send_message(message.chat.id, 'В каком мессенджере с Вами связаться?',
                                          reply_markup=self.keyboard_messenger)
                    self.bot.register_next_step_handler(message, self.messanger)  # in which method of the class to
                # wait for the next message

                else:
                    self.check_messenger(message)  # checking whether the data is up-to-date

            else:  # if the connection does not exist
                self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def messanger(self, message):   # get a message from the messenger menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'WhatsApp':  # if message text is 'WhatsApp'
                requests_sql.update_messanger(self.conn, message.chat.id, 'WhatsApp')  # write messenger name of to
                # the database
                self.bot.send_message(message.chat.id,
                                      'Введите свой номер телефона в формате +79ХХХХХХХХХ '
                                      'и Я с Вами свяжусь в ближайшее время!\n'
                                      'Знак "+" вводить обязательно!', reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.number_or_username)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Instagram':  # if message text is  'Instagram'
                requests_sql.update_messanger(self.conn, message.chat.id, 'Instagram')  # write messenger name of to
                # the database
                self.bot.send_message(message.chat.id,
                                      'Введите свой аккаунт в формате @yourname '
                                      'и Я с Вами свяжусь в ближайшее время!\n'
                                      'Знак "@" вводить обязательно!', reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.number_or_username)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Telegram':  # if message text is 'Telegram'
                requests_sql.update_messanger(self.conn, message.chat.id, 'Telegram')  # write messenger name of to
                # the database
                self.bot.send_message(message.chat.id,
                                      'Введите свой номер телефона в формате +79ХХХХХХХХХ или имя пользователя '
                                      'в формате @yourname и Я с Вами свяжусь в ближайшее время!\n'
                                      'Знак "+" или "@" вводить обязательно!', reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.number_or_username)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def number_or_username(self, message):   # get a message from phone number/username
        if self.conn:  # checking if the connection exists
            if '+' in message.text.strip() or '@' in message.text.strip():  # if '+' or '@' in message text
                requests_sql.update_number_or_username(self.conn, message.chat.id, message.text)  # write phone
                # number/username of to the database
                self.close_order(message)  # close order

            else:  # if not '+' or '@' in message text
                self.bot.send_message(message.chat.id, 'Знаки "+" или "@" вводить обязательно!'
                                                       'Попробуйте еще раз!', reply_markup=types.ReplyKeyboardRemove())
                self.bot.register_next_step_handler(message, self.number_or_username)  # in which method of the class to
                # wait for the next message

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def check_messenger(self, message):   # get a message from the check messenger and phone number/username
        if self.conn:  # checking if the connection exists
            messanger_and_number = requests_sql.get_messenger_and_number(self.conn, message.chat.id)  # get messenger
            # name and phone number/username
            self.bot.send_message(message.chat.id, f'С Вами связаться в {messanger_and_number[0][0]}, '
                                                   f'{messanger_and_number[0][1]}',
                                  reply_markup=self.keyboard_yes_or_no)
            self.bot.register_next_step_handler(message, self.messenger_yes_or_no)  # in which method of the class to
            # wait for the next message

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def messenger_yes_or_no(self, message):  # get a message from yes or no menu
        if self.conn:  # checking if the connection exists
            if message.text.strip() == 'Да':  # if message text is 'Да'
                self.close_order(message)  # close order

            elif message.text.strip() == 'Нет':  # if message text is 'Нет'
                self.bot.send_message(message.chat.id, 'В каком мессенджере с Вами связаться?',
                                      reply_markup=self.keyboard_messenger)
                self.bot.register_next_step_handler(message, self.messanger)  # in which method of the class to
                # wait for the next message

            elif message.text.strip() == 'Главное меню':  # if message text is 'Главное меню'
                self.bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=self.keyboard_main)
                self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

    def close_order(self, message):  # close order
        if self.conn:  # checking if the connection exists
            information = requests_sql.get_all(self.conn, message.chat.id)  # get all from the database
            self.bot.send_message(chat_id=my_id,
                                  text=f'Десерт: {str(information[0][1])}\n'
                                       f'Количество: {str(information[0][2])}\n'
                                       f'Имя: {str(information[0][6])}\n'
                                       f'Номер или логин: {str(information[0][5])}\n'
                                       f'Мессенджер: {str(information[0][3])}\n'
                                       f'Цена: {str(int(information[0][4]))}\n'
                                       f'Дата: {str(information[0][7])}\n'
                                       f'Декор: {str(information[0][8])}',
                                  reply_markup=types.ReplyKeyboardRemove())

            self.bot.send_message(message.chat.id, f'В ближайшее время Я с Вами свяжусь в {str(information[0][3])}, '
                                                   f'{str(information[0][5])}!\n'
                                                   f'Спасибо!',
                                  reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

        else:  # if the connection does not exist
            self.bot.send_message(message.chat.id, 'Ошибка, попробуйте позже', reply_markup=self.keyboard_main)
            self.bot.register_next_step_handler(message, self.main_menu)  # back to main menu

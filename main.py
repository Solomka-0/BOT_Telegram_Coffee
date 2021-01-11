# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
import data
import ast
import math
import json
import time

import requests
from yandex import Translater
from bs4 import BeautifulSoup as BS
import speech_controller
import speech

''' ------ Инициализация ------ '''
ANSWERS = {'start_msg':'Приветствую. Я Coffee. Если ты не против, то я могу каждую неделю присылать тебе контакты человека, готового пообщаться. Это поможет тебе расслабится, найти друга, или, напротив, твоего противника, но, в любом случае, тебе будет интересно 😉\nСначала ты можешь подписаться, для этого просто нажми на кнопку ниже ↓',
'subs_correctly':'Прекрасно! Ты подписался на рассылку.\nТеперь можешь найти себе человека для общения: /find_couple',
'subs_wrong':'Ты уже подписан!',
'unsubs_correctly':'Отписался? - Возвращайся: /subscribe',
'unsubs_wrong':'Ты не подписан! Скорее подпишись: /subscribe',
'no_username':'Обязательно укажи свой username иначе собеседник не сможет тебя найти. Это можно сделать в настройках:\nНАСТРОЙКИ >> ИЗМЕНИТЬ ПРОФИЛЬ >> ИМЯ ПОЛЬЗОВАТЕЛЯ',
'information_without_lastname':'Познакомся, это %s. Можешь написать ему(ей), вот ссылка на профиль: @%s',
'information_with_lastname':'%s - отныне твой твой собеседник. Напиши первым: @%s',
'no_couple': 'Для вас не было найдено пары. Напишите через некоторое время или подождите: собеседник сам вас найдет',
'no_subscribe': 'Ты еще не подписан?!? - /subscribe'
}

BOT = telebot.TeleBot(data.token)

''' ------ Функциии ------ '''
class Subs(object): # Класс отвечает за сохранение листа в текстовом файле, его чтение и редактирование
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename + '.json') as file:
                self.list = json.load(file).copy()
                file.close()
        except:
            self.list = []
    def saving(self): # Перезаписывает(сохраняет) лист
        with open(self.filename + '.json', 'w') as file:
            json.dump(self.list, file)
            file.close()
    def find_value(self, key, value): # Находит элемент словаря в листе
        for element in self.list:
            if element[key] == value:
                return element
        return False
    def add(self, element): # Добавляет элемент в лист и перезаписывает(сохраняет) его
        self.list.append(element)
        self.saving()
    def withdraw(self, key, value): # Удаляет элемент из листа и перезаписывает(сохраняет) его
        self.list.remove(self.find_value(key, value))
        self.saving()



def contact_details_output(element): # Возвращает строку с информацией о пользователе
    global ANSWERS
    if element['last_name'] == None:
        return ANSWERS['information_without_lastname'] % (element['first_name'], element['username'])
    else:
        return ANSWERS['information_with_lastname'] % (element['first_name'] + ' ' + element['last_name'], element['username'])

def subscribe_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_0 = types.InlineKeyboardButton(text='- Найти пару -', callback_data = 'call_find_couple')
    button_1 = types.InlineKeyboardButton(text='- Информация о подписчиках -', callback_data = 'call_info')
    button_2 = types.InlineKeyboardButton(text='- Отписаться -', callback_data = 'call_unsubscribe')
    markup.add(button_0, button_1, button_2)
    return markup

def selection(id, array, rank):
    global rating
    max_rank = 0
    difference = 100;
    for element in array.list[id:id + 3]:
        if difference > math.fabs(rank - (rating.find_value('chat_id', element['chat_id'])['rating'])):
            rating.find_value('chat_id', element['chat_id'])['rating']
    return array.list[0]

def est_markup(id):
    global rating
    markup = types.InlineKeyboardMarkup()
    like_button = types.InlineKeyboardButton(text='- Он(она) мне нравится 👍 -', callback_data = 'like' + str(id) + '_' + str(rating.find_value('chat_id', id)['rating']+1))
    dislike_button = types.InlineKeyboardButton(text='- Мне не нравится/не подходит этот человек 👎-', callback_data = 'dislike' + str(id) + '_' + str(rating.find_value('chat_id', id)['rating']-1))
    markup.add(like_button, dislike_button)
    return markup

@BOT.message_handler(commands = ['find_couple']) # Ищет второго собеседника
def find_couple(message):
    global subs, ANSWERS, rating
    persons = []
    if subs.find_value('chat_id', message.chat.id):
        pass
    else:
        BOT.send_message(message.chat.id, ANSWERS['no_subscribe'])
        return

    if len(subs.list) > 1:
        persons.append(subs.find_value('chat_id', message.chat.id))
        subs.withdraw('chat_id', message.chat.id)
        persons.append(selection(random.randint(0, len(subs.list)-1), subs, rating.find_value('chat_id', message.chat.id)['rating']))
        BOT.send_message(message.chat.id, contact_details_output(persons[1]), reply_markup = est_markup(persons[1]['chat_id']))
        BOT.send_message(persons[1]['chat_id'], contact_details_output(persons[0]), reply_markup = est_markup(message.chat.id))
        subs.withdraw('chat_id', persons[1]['chat_id'])
    else:
        BOT.send_message(message.chat.id, ANSWERS['no_couple'])
        return

@BOT.message_handler(commands = ['unsubscribe']) # Отписывает пользователя от рассылки
def unsubscribe(message):
    global subs, ANSWERS
    if subs.find_value('chat_id', message.chat.id):
        subs.withdraw('chat_id', message.chat.id)
        BOT.send_message(message.chat.id, ANSWERS['unsubs_correctly'])
    else:
        BOT.send_message(message.chat.id, ANSWERS['unsubs_wrong'])

@BOT.message_handler(commands = ['subscribe']) # Подписывает пользователя на рассылку
def subscribe(message):
    global subs, ANSWERS,rating
    if rating.find_value('chat_id', message.chat.id) == False:
        rating.add({'chat_id':message.chat.id, 'rating':10})
    if message.chat.username == None:
        BOT.send_message(message.chat.id, ANSWERS['no_username'])
        return
    if subs.find_value('chat_id', message.chat.id):
        BOT.send_message(message.chat.id, ANSWERS['subs_wrong'], reply_markup = subscribe_markup())
    else:
        subs.add({'chat_id':message.chat.id, 'username':message.chat.username, 'first_name':message.chat.first_name, 'last_name':message.chat.last_name})
        BOT.send_message(message.chat.id, ANSWERS['subs_correctly'], reply_markup = subscribe_markup())

@BOT.message_handler(commands = ['info']) # Выводит информацию о всех подписчиках
def info(message):
    global subs
    BOT.send_message(message.chat.id, f'Подписанные пользователи [{len(subs.list)}]:')
    for sub in subs.list:
        name = sub['first_name'] + ' ' + str(sub['last_name'])
        BOT.send_message(message.chat.id, f'- {name}')

@BOT.message_handler(commands = ['start', 'help'])
def start(message):
    global rating
    if rating.find_value('chat_id', message.chat.id) == False:
        rating.add({'chat_id':message.chat.id, 'rating':10})
    start_markup = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton(text='- Подписаться -', callback_data = 'call_subscribe')
    start_markup.add(start_button)
    BOT.send_message(message.chat.id, ANSWERS['start_msg'], reply_markup = start_markup)


@BOT.message_handler(content_types = ['text']) # Обрабатывает текстовые сообщения
def repeat_all_messages(message):
    global user_variables
    BOT.send_chat_action(message.chat.id, "typing")

    print(user_variables.find_value('chat_id', message.chat.id))
    if not user_variables.find_value('chat_id', message.chat.id):
        user_variables.add({'chat_id':message.chat.id, 'typing':True})

    request = message.text #Сообщение от пользователя
    request = request.lower()
    words = [] # Массив со словами из сообщения
    id_w_list = [] # Массив, который хранит в себе ID ключевых слов
    words = speech.text_in_words(speech.remove_characters(request)) # Перевод текста в слова с удалением запятых
    words = speech.del_spaces(words) # Удаление пустых элементов в массиве
    id_w_list = speech.words_in_ids(words) # Определяет ключевые слова в массиве со словами
    try:
        answer = speech_controller.answer(id_w_list, message.chat.first_name, message.chat.id, words, request)
        if user_variables.find_value('chat_id', message.chat.id)['typing'] == True:
            time.sleep(len(answer)/25)
        BOT.send_message(message.chat.id, answer)
    except:
        pass

def delete_markup(message):
    BOT.edit_message_text(chat_id = message.chat.id, message_id = message.message_id, text = message.text)

@BOT.callback_query_handler(lambda call: ("like" in call.data) or ("dislike" in call.data))
def call_est(call):
    global rating
    if 'dislike' in call.data:
        # Обработка
        call.data = call.data.replace('dislike','')
        id = int(call.data[0:call.data.find('_')])
        rank = int(call.data[call.data.find('_')+1:len(call.data)])
        # Сохранение
        rating.withdraw('chat_id', id)
        rating.add({'chat_id':id, 'rating':rank})
        delete_markup(call.message)
    elif 'like' in call.data:
        # Обработка
        call.data = call.data.replace('like','')
        id = int(call.data[0:call.data.find('_')])
        rank = int(call.data[call.data.find('_')+1:len(call.data)])
        # Сохранение
        rating.withdraw('chat_id', id)
        rating.add({'chat_id':id, 'rating':rank + 1})
        delete_markup(call.message)

@BOT.callback_query_handler(lambda call: call.data=="call_subscribe")
def call_subscribe(call):
    subscribe(call.message)
    delete_markup(call.message)

@BOT.callback_query_handler(lambda call: call.data=="call_unsubscribe")
def call_unsubscribe(call):
    unsubscribe(call.message)
    delete_markup(call.message)

@BOT.callback_query_handler(lambda call: call.data=="call_info")
def call_info(call):
    info(call.message)
    delete_markup(call.message)

@BOT.callback_query_handler(lambda call: call.data=="call_find_couple")
def call_find_couple(call):
    find_couple(call.message)
    delete_markup(call.message)

user_variables = Subs('user_variables') # Создает отдельный лист с переменными данными для пользователей
subs = Subs('subscribers') # Создает лист с подписчиками
rating = Subs('rating') # Создает отдельный лист с рейтингом

if __name__ == '__main__':
    BOT.polling(none_stop=True)

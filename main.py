import telebot
import random
import data
import ast

answers = {'start_msg':'Приветствую. Я - Coffee. Если ты не против, то я могу каждую неделю присылать тебе контакты человека, готового пообщаться. Это поможет тебе расслабится, найти друга, или, напротив, твоего противника, но, в любом случае, тебе будет интересно. \nДля начала ты можешь подписаться: /subscribe, - а дальше я тебе все объясню',
'subs_correctly':'Прекрасно! Вы подписались на рассылку.\nТеперь вы можете найти себе человека для общения: /find_couple',
'subs_wrong':'Вы уже подписаны.',
'unsubs_correctly':'Отписались? - Возвращайтесь: /subscribe',
'unsubs_wrong':'Вы не подписаны! Подпишитесь: /subscribe',
'no_username':'Обязательно укажите свой username иначе ваш собеседник не сможет вас найти. Это можно сделать в настройках:\nНАСТРОЙКИ >> ИЗМЕНИТЬ ПРОФИЛЬ >> ИМЯ ПОЛЬЗОВАТЕЛЯ',
'information_without_lastname':'Познакомся, это %s. Можешь написать ему(ей), вот ссылка на профиль: @%s',
'information_with_lastname':'%s - отныне твой твой собеседник. Напиши первым: @%s',
'no_couple': 'Для вас не было найдено пары. Напишите через некоторое время или подождите: собеседник сам вас найдет',
'no_subscribe': 'Вы не подписаны! /subscribe'
}

misund_msg = ['Не понял, о чем ты?!', 'Что это значит?😅', 'Наверное ты ошибься', '-❓❔❓❔❓-', 'Не понимаю 😥', 'Серьезно?']

bot = telebot.TeleBot(data.token)

class Subs(object): # Класс отвечает за сохранение листа в текстовом файле, его чтение и редактирование
    def __init__(self, filename):
        self.filename = filename
        try:
            array = []
            file = open(self.filename + '.txt')
            for line in file:
                array.append(ast.literal_eval(line))
            file.close()
            self.list = array
        except:
            self.list = []
    def saving(self): # Перезаписывает(сохраняет) лист
        file = open(self.filename + '.txt', 'w')
        for element in self.list:
             file.write(str(element))
             file.write('\n')
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
    global answers
    if element['last_name'] == None:
        return answers['information_without_lastname'] % (element['first_name'], element['username'])
    else:
        return answers['information_with_lastname'] % (element['first_name'] + ' ' + element['last_name'], element['username'])

@bot.message_handler(commands=['find_couple']) # Ищет второго собеседника
def find_couple(message):
    global subs, answers
    persons = []
    if subs.find_value('chat_id', message.chat.id):
        pass
    else:
        bot.send_message(message.chat.id, answers['no_subscribe'])
        return

    if len(subs.list) > 1:
        persons.append(subs.find_value('chat_id', message.chat.id))
        subs.withdraw('chat_id', message.chat.id)
        persons.append(subs.list[random.randint(0, len(subs.list)-1)])
        bot.send_message(message.chat.id, contact_details_output(persons[1]))
        bot.send_message(persons[1]['chat_id'], contact_details_output(persons[0]))
        subs.withdraw('chat_id', persons[1]['chat_id'])
    else:
        bot.send_message(message.chat.id, answers['no_couple'])
        return

@bot.message_handler(commands=['unsubscribe']) # Отписывает пользователя от рассылки
def unsubscribe(message):
    global subs, answers
    if subs.find_value('chat_id', message.chat.id):
        subs.withdraw('chat_id', message.chat.id)
        bot.send_message(message.chat.id, answers['unsubs_correctly'])
    else:
        bot.send_message(message.chat.id, answers['unsubs_wrong'])

@bot.message_handler(commands=['subscribe']) # Подписывает пользователя на рассылку
def subscribe(message):
    global subs, answers
    if message.chat.username == None:
        bot.send_message(message.chat.id, answers['no_username'])
        return
    if subs.find_value('chat_id', message.chat.id):
        bot.send_message(message.chat.id, answers['subs_wrong'])
    else:
        subs.add({'chat_id':message.chat.id, 'username':message.chat.username, 'first_name':message.chat.first_name, 'last_name':message.chat.last_name})
        bot.send_message(message.chat.id, answers['subs_correctly'])

@bot.message_handler(commands=['info']) # Выводит информацию о всех подписчиках
def info(message):
    global subs
    bot.send_message(message.chat.id, f'Подписанные пользователи [{len(subs.list)}]:')
    for sub in subs.list:
        name = sub['first_name'] + ' ' + str(sub['last_name'])
        bot.send_message(message.chat.id, f'- {name}')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, answers['start_msg'])

@bot.message_handler(content_types=['text']) # Обрабатывает текстовые сообщения
def repeat_all_messages(message):
    global misund_msg
    bot.send_message(message.chat.id, misund_msg[random.randint(0, len(misund_msg)-1)])

subs = Subs('subscribers') # Создает лист с подписчиками

if __name__ == '__main__':
    bot.polling(none_stop=True)

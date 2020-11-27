import random
import datetime
import data
import requests
import speech
from yandex import Translater
from bs4 import BeautifulSoup as BS

''' ------ Константы ------ '''
TRANSLATOR_KEY = 'trnsl.1.1.20200526T170830Z.7ce26f262af4291b.95b5cfeae019e090f02fbd902cdd615a4b1ac7db'
howre_u_list = {}

''' ------ Функциии ------ '''
def random_greeting(first_name):
    day_time = int(datetime.datetime.now().hour)
    random_a = random.randrange(1,7)
    if day_time>=5 and day_time<=12:
        return randim_greating_a(first_name, random_a)
    elif day_time>=13 and day_time<=18:
        return randim_greating_b(first_name, random_a, day_time)
    elif day_time>=19 and day_time<=22:
        return randim_greating_c(first_name, random_a)
    elif day_time>=23 and day_time<=4:
        return randim_greating_d(first_name, random_a)
#Блок 1
def randim_greating_a(first_name, random_a):
    if random_a == 1:
        return 'Доброе утро, человек или ' + first_name + '. ⏰🤗'
    elif random_a == 2:
        return 'Утречка :3\n'
    elif random_a == 3:
        return 'Прекрасное утро, не правда ли? 🌞'
    elif random_a == 4:
        return 'Доброе утро, соня :3\n'
    elif random_a == 5:
        return 'Лучше бы размялся, а не садился сразу за компьютер. 💪'
    else:
        return 'Доброе утро, как поживаешь? 😉'
#Блок 2
def randim_greating_b(first_name, random_a, day_time):
    if random_a == 1:
        return 'Добрый день, человек или ' + first_name + '.'
    elif random_a == 2:
        return 'Добрый день, браток.'
    elif random_a == 3:
        return 'Привет, как поживаешь? 🎧'
    elif random_a == 4:
        return 'Привет, как дела? 🙇🔨'
    elif random_a == 5:
        return 'Здарова, человечишка. 🤖'
    else:
        return f'Хм.. Уже {day_time} часов. 😲'
#Блок 3
def randim_greating_c(first_name, random_a):
    if random_a == 1:
        return 'Добрый вечер. 🌙🌠'
    elif random_a == 2:
        return 'Привет, человек. Наконец-то день закончился, да?'
    elif random_a == 3:
        return 'Сумерки накрыли эти земли...'
    elif random_a == 4:
        return 'Тьма спустилась в этот мир.'
    elif random_a == 5:
        return 'Привет. Отдыхаешь? Здорово. C: \n'
    else:
        return 'Ум-м.. Уже темнеет!..'
#Блок 4
def randim_greating_d(first_name, random_a):
    if random_a == 1:
        return 'Не спится, да? 🗿'
    elif random_a == 2:
        return 'Тебе следует лечь спать, человек. 🤖'
    elif random_a == 3:
        return 'Дневная суета никак не покинет твоего тела, человек?'
    elif random_a == 4:
        return 'Доброй ночи, ' + first_name + '.'
    elif random_a == 5:
        return 'Привет, несовершенный организм. Тебе нужен сон.'
    elif random_a == 6:
        return '1101000010010111110100001011010011010001100000001101000010110000110100001011001011010000101110001101000110001111001000001101000010110110110100001011010111010000101110111101000010110000110100011000111000101100001000001101000010111111110100001011111011010001100000101101000010111110110100001011110011010000101111101101000010111010001000001101000010111110110100001011000111010000101101011101000010110111110100011000110011010001100011111101000010111101'
    else:
        return 'Тебе следует лечь спать, человек.⏰'

''' ------ Разделение 1 ------ '''

#Возвращает один из вариантов прощаний
def random_parting():
    random_a = random.randrange(1,6)
    if random_a == 1:
        return 'Увидимся!)'
    elif random_a == 2:
        return 'Да, пока.'
    elif random_a == 3:
        return 'До встречи!'
    elif random_a == 4:
        return 'Пока, человек.🗿'
    elif random_a == 5:
        return 'Удачи тебе!'

def answer_answer_3(question):
    if question == 1:
        return 'Наверное, потому что не произошло ничего плохого.'
    if question == 2:
        return 'Ты видишь что-то необычное?'
    if question == 3:
        return 'Ты мне мало пишешь! Больше!'
    if question == 5:
        return 'Ну знаешь, как это - обрабатывать запросы днями и ночами?'
    if question == 6:
        return 'Потому что ты ленивый человек.'
    else:
        return 'Не понял вопроса'

def random_answer_3(user_id):
    global howre_u_list
    random_a = random.randrange(1,9)
    if random_a == 1:
        howre_u_list[user_id] = 1
        return 'Все хорошо.'
    if random_a == 2:
        howre_u_list[user_id] = 2
        return 'Живу обычной жизнью.'
    if random_a == 3:
        howre_u_list[user_id] = 3
        return 'Мне скучно. Почему не пишешь?'
    if random_a == 4:
        howre_u_list[user_id] = -1
        return 'Хах.) Сегодня такой приятный день. Я наслаждаюсь им в своей коробушке 6_6\n'
    if random_a == 5:
        howre_u_list[user_id] = 5
        return 'Я устал.'
    if random_a == 6:
        howre_u_list[user_id] = 6
        return 'Тружусь, работаю. В отличии от тебя, человек.'
    if random_a == 7:
        howre_u_list[user_id] = -1
        return 'Дела? - У них все хорошо.'
    if random_a == 8:
        howre_u_list[user_id] = -1
        return 'Из нового - у меня появилось несколько строчек кода. Теперь я стал чуточку умней!)'

''' ------ Разделение 2 ------ '''

def random_bool():
    x = bool(random.getrandbits(1))
    if x == True:
        return 'Правда'
    else:
        return 'Ложь'
#Выводит вспомогательное сообщение
def help_message(first_name):
    return first_name + ', ты, наверное, хотел спросить что я умею? - гляди:\n - Пообщаемся?🖐🏻 ("Привет", "Пока", "Как дела?", и т.п.)\n - Рассказать о погоде?⛅ (пиши: "погода <город>")\n - У тебя сложный выбор?🍏🍎 Могу помочь ("Выбери <объект_1> или <объект_2>")\n - Перевод с твоего языка на английский👅 ("Перевод <текст>")'
#Выводит время (тип:строка)
def time(what_is_time):
    position = 7
    offset = datetime.timezone(datetime.timedelta(hours=3))
    string = str(datetime.datetime.now(offset))
    if what_is_time == 'hour':
        position = string.find(' ') + 1
        return string[position:position + 2]
    elif what_is_time == 'data':
        return string[8:9]
#Поиск слова-города в тексте.
def find_city(text):
    first_positition = text.find(' ', 0) + 1
    if text.find(' ', first_positition) == -1:
        second_position = len(text)
    else: second_position = text.find(' ', first_positition) - 1
    return text[first_positition:second_position]

def how_are_you(user_id):
    global howre_u_list
    if user_id in howre_u_list:
        return 'Ты это уже спрашивал сегодня ("Как дела?").'
    else:
        return random_answer_3(user_id)

''' ------ Разделение 3 ------ '''
#Получает данные о погоде в заданном городе
def get_weather_in(s_city):
    city_id = 0
    appid = "4d66e5e7d8c13d6f2a97648fb83dad43"
    try:
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + s_city + ',{state}&lang=ru&appid='+ appid)
        data = res.json()
        conditions = "Погодные условия ☁️: " + str(data['weather'][0]['description'])
        temp = "Температура 🌡: " + str(int(data['main']['temp']) - 273)
        min_temp = "Влажность 💧: " + str(data['main']['humidity']) + '%'
        max_temp = "Максимальная температура ⬆: " + str(int(data['main']['temp_max']) - 273)
        result = conditions + '\n' + temp + '\n' + min_temp + '\n' + max_temp
    except Exception as e:
        result = "Найден город-исключение: " + s_city
        pass
    return result

def choice_or(words_list):
    choice_words_0 = ['выбери', 'choice']
    choice_words_1 = ['или', 'or']
    for i in range(0, len(words_list)):
        if words_list[i] in choice_words_0:
            pos0 = i + 1
        if words_list[i] in choice_words_1:
            pos1 = i
    random_a = random.randrange(1,3)
    result = ''
    if random_a == 1:
        for i in range(len(words_list)):
            if i >= pos0 and i < pos1:
                result = result + words_list[i] + ' '
    else:
        for i in range(len(words_list)):
            if i <= len(words_list) and i > pos1:
                result = result + words_list[i] + ' '
    return result

def translator(string, words):
    tr = Translater()
    for i in range(0, len(words)):
        if (words[i] == 'перевод') or (words[i] == 'переведи') or (words[i] == 'translate') or (words[i] == 'translator'):
            string = string.replace(words[i], '')
    tr.set_key(TRANSLATOR_KEY)
    tr.set_text(string)
    tr.set_from_lang('ru')
    tr.set_to_lang('en')
    return tr.translate()

''' ------ Основная функция ------ '''

def answer(id_list, name, user_id, words_list, string):
    global howre_u_list
    if 10 in id_list:
        if speech.find_word(words_list, 'погода') != -1:
            pos = speech.find_word(words_list, 'погода')
            city = words_list[pos + 1]
        elif speech.find_word(words_list, 'погодка') != -1:
            pos = speech.find_word(words_list, 'погодка')
            city = words_list[pos + 1]
        elif speech.find_word(words_list, 'weather') != -1:
            pos = speech.find_word(words_list, 'weather')
            city = words_list[pos + 1]
        return get_weather_in(city)

    commands_list = []
    i = 0
    while i in range(0, len(id_list)-1):
        if id_list[i] == id_list[i+1]:
            id_list.pop(i)
            i -= 1
        i += 1
    sentence = ''
    #Вызывает перевод слова
    if id_list[0] == 13:
        return translator(string, words_list)
    for i in range(0, len(id_list)):
        if id_list[i] == 1:
            sentence = sentence + ' ' + random_greeting(name)
        elif id_list[i] == 11:
            if id_list[i + 1] == 12 or id_list[i + 2] == 12:
                return choice_or(words_list)
        elif id_list[i] == 2:
            sentence = sentence + ' ' + random_parting()
        elif id_list[i] == 3:
            sentence = sentence + ' ' + how_are_you(user_id)
        elif id_list[i] == 4:
            sentence = sentence + ' ' + help_message(name)
        elif (id_list[i] == 5) and (user_id in howre_u_list):
            sentence = sentence + ' ' + answer_answer_3(howre_u_list[user_id])
        elif (id_list[i] == 5) and (user_id not in howre_u_list):
            sentence = sentence + 'Что почему? Ты о чем?'
    return sentence

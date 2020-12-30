import random
import datetime
import data
import requests
import speech
from yandex import Translater
from bs4 import BeautifulSoup as BS


''' ------ Функциии ------ '''
def random_greeting(first_name):
    day_time = int(datetime.datetime.now().hour)
    if day_time>=5 and day_time<=12:
        return morning_greeting(first_name)
    elif day_time>=13 and day_time<=18:
        return afternoon_greeting(first_name, day_time)
    elif day_time>=19 and day_time<=22:
        return evening_greeting(first_name)
    elif day_time>=23 and day_time<=4:
        return night_greeting(first_name)

# Утренние приветствия
def morning_greeting(first_name):
    greating_list = [f'Доброе утро, человек или {first_name}. ⏰🤗', 'Утречка :3\n', 'Прекрасное утро, не правда ли? 🌞',
    'Доброе утро, соня :3\n', 'Лучше бы размялся, а не садился сразу за компьютер. 💪', 'Доброе утро, как поживаешь? 😉']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Дневные приветствия
def afternoon_greeting(first_name, day_time):
    greating_list = [f'Добрый день, человек или {first_name}.', 'Добрый день, браток.', 'Привет, как поживаешь? 🎧',
    'Привет, как дела? 🙇🔨', 'Здарова, человечишка. 🤖', f'Хм.. Уже {day_time} часов. 😲']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Вечерние приветствия
def evening_greeting(first_name):
    greating_list = ['Добрый вечер. 🌙🌠', 'Привет, человек. Наконец-то день закончился, да?', 'Сумерки накрыли эти земли...',
    'Тьма спустилась в этот мир.', 'Привет. Отдыхаешь? Здорово. C: \n', 'Ум-м.. Уже темнеет!..']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Ночные приветствия
def night_greeting(first_name):
    greating_list = ['Не спится, да? 🗿', 'Тебе следует лечь спать, человек. 🤖',
    'Дневная суета никак не покинет твоего тела, человек?', f'Доброй ночи, {first_name}.', 'Привет, несовершенный организм. Тебе нужен сон.'
    '1101000010010111110100001011010011010001100000001101000010110000110100001011001011010000101110001101000110001111001000001101000010110110110100001011010111010000101110111101000010110000110100011000111000101100001000001101000010111111110100001011111011010001100000101101000010111110110100001011110011010000101111101101000010111010001000001101000010111110110100001011000111010000101101011101000010110111110100011000110011010001100011111101000010111101'
    'Тебе следует лечь спать, человек.⏰']
    return greating_list[random.randint(0, len(greating_list)-1)]

''' ------ Разделение 1 ------ '''

# Возвращает один из вариантов прощаний
def parting():
    parting_list = ['Увидимся!)', 'Да, пока.', 'До встречи!',
    'Пока, человек.🗿', 'Удачи тебе!']
    return parting_list[random.randint(0, len(parting_list)-1)]

''' ------ Разделение 2 ------ '''

#Выводит вспомогательное сообщение
def help_message(first_name):
    return first_name + ''', ты, наверное, хотел спросить что я умею? - гляди:
     - Пообщаемся?🖐🏻 ("Привет", "Пока", "Как дела?", и т.п.)
     - Рассказать о погоде?⛅ (пиши: "погода <город>")
     - У тебя сложный выбор?🍏🍎 Могу помочь ("Выбери <объект_1> или <объект_2>")
     - Перевод с твоего языка на английский👅 ("Перевод <текст>")'''

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

def bot_mood(user_id):
    mood_list = ['Все хорошо.', 'Живу обычной жизнью.', 'Мне скучно. Почему не пишешь?',
    'Хах.) Сегодня такой приятный день. Я наслаждаюсь им в своей коробушке 6_6\n', 'Я устал.',
    'Тружусь, работаю. В отличии от тебя, человек.', 'Дела? - У них все хорошо.',
    'Из нового: у меня появилось несколько строчек кода. Теперь я стал чуточку умней!)']
    return mood_list[random.randint(0, len(mood_list)-1)]

''' ------ Разделение 3 ------ '''
#Получает данные о погоде в заданном городе
def get_weather_in(s_city):
    city_id = 0
    try:
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + s_city + ',{state}&lang=ru&appid='+ data.OPENWEATHEMAP_KEY)
        w_data = res.json()
        conditions = "Погодные условия ☁️: " + str(w_data['weather'][0]['description'])
        temp = "Температура 🌡: " + str(int(w_data['main']['temp']) - 273)
        min_temp = "Влажность 💧: " + str(w_data['main']['humidity']) + '%'
        max_temp = "Максимальная температура ⬆: " + str(int(w_data['main']['temp_max']) - 273)
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
    tr.set_key(data.TRANSLATOR_KEY)
    tr.set_text(string)
    tr.set_from_lang('ru')
    tr.set_to_lang('en')
    return tr.translate()

''' ------ Основная функция ------ '''

def answer(id_list, name, user_id, words_list, string):

    if 10 in id_list: # Возвращает погоду в выбранном городе
        weather_words = ['погода', 'weather']
        for i in range(0, len(weather_words)):
            if speech.find_word(words_list, weather_words[i]) != -1:
                return get_weather_in(words_list[speech.find_word(words_list, weather_words[i]) + 1])
    i = 0
    while i in range(0, len(id_list)):
        if id_list.count(id_list[i]) > 1:
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
            sentence = sentence + ' ' + parting()
        elif id_list[i] == 3:
            sentence = sentence + ' ' + bot_mood(user_id)
        elif id_list[i] == 4:
            sentence = sentence + ' ' + help_message(name)
        elif id_list[i] == 5:
            sentence = sentence + 'Что почему? Ты о чем?'
    return sentence

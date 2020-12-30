from inspect import getsourcefile
from os.path import abspath
OPENWEATHEMAP_KEY = "<Ваш токен>" # Место для токена API openweathermap
TRANSLATOR_KEY = '<Ваш токен>' # Место для токена yandex-переводчика
token = "<Ваш токен>" # Место для токена сообщества
path = abspath(getsourcefile(lambda:0)).replace('\\', '/').replace('data.py','') # Определение пути к папке
print('\n\033[32m\033[40mТокен сообщества: \033[33m\033[40m' + str(token[0:8]) + '-...-' + str(token[len(token)-8:len(token)]))
print('\n\033[32m\033[40mТокен из openweathermap: \033[33m\033[40m' + str(OPENWEATHEMAP_KEY[0:8]) + '-...-' + str(OPENWEATHEMAP_KEY[len(OPENWEATHEMAP_KEY)-8:len(OPENWEATHEMAP_KEY)]))
print('\033[32m\033[40mТекущий путь к папке: \033[33m\033[40m' + path + '\033[37m\033[40m')

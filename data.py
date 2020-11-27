from inspect import getsourcefile
from os.path import abspath
OPENWEATHEMAP_ID = "<Ваш токен>" # Место для токена API openweathermap
token = "<Ваш токен>" # Место для токена сообщества
path = abspath(getsourcefile(lambda:0)).replace('\\', '/').replace('data.py','') # Определение пути к папке
print('\n\033[32m\033[40mТокен сообщества: \033[33m\033[40m' + str(token[0:8]) + '-...-' + str(token[len(token)-8:len(token)]))
print('\n\033[32m\033[40mТокен из openweathermap: \033[33m\033[40m' + str(OPENWEATHEMAP_ID[0:8]) + '-...-' + str(OPENWEATHEMAP_ID[len(OPENWEATHEMAP_ID)-8:len(OPENWEATHEMAP_ID)]))
print('\033[32m\033[40mТекущий путь к папке: \033[33m\033[40m' + path + '\033[37m\033[40m')

ALPHABET = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ь','э','ю','я','ы',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', ' ']

KEY_WORDS = {'привет':1,'прив':1,'добрый день':1,'эй':1,'приветики':1,'приветик':1,'хай':1,'хелло':1,'hi':1,'hello':1,
'пока':2,'поки':2,'до встречи':2,'прощай':2,'bye':2,'good bye':2,
'помоги':4,'помощь':4, 'help':4,
'как дела':3,'как ты':3,'что нового':3, 'how are you':3,
'почему':5, 'why':5,
'погода':10, 'погодка':10, 'weather':10,
'выбери':11,'choice':11,'или':12, 'or':12,
'перевод':13, 'переведи':13, 'translator':13, 'translate':13}

# Удаляет лишние пробелы в словарном листе
def del_spaces(array_of_words):
    i = 0
    while i < len(array_of_words):
        if array_of_words[i] == '':
            array_of_words.pop(i)
            i -= 1
        i += 1
    return array_of_words

# Выносит из массива ключи
def words_in_ids(array_of_words):
    global KEY_WORDS
    array_of_words = del_spaces(array_of_words)
    id_list = []
    for i in range(0, len(array_of_words)):
        if array_of_words[i] in KEY_WORDS:
            id_list.append(KEY_WORDS[array_of_words[i]])
        if i < len(array_of_words) - 1:
            if (array_of_words[i] + ' ' + array_of_words[i+1]) in KEY_WORDS:
                x = array_of_words[i] + ' ' + array_of_words[i+1]
                id_list.append(KEY_WORDS[x])
    return id_list

# Переводит строку в массив со словами
def text_in_words(string):
    string = remove_characters(string)
    k = []
    while string.find(' ') > -1:
        pos = string.find(' ')
        k.append(string[0:pos])
        string = string[pos+1:len(string)]
    k.append(string)
    return k

# Проверяет допустим ли символ
def in_the_array(char):
    global ALPHABET
    bool = False
    for i in range(0, len(ALPHABET)):
        if char == ALPHABET[i]:
            bool = True
    return bool

# Возврщает массив, в котором два элемента - начало и конец "многобуквия"
def repetition(string):
    for i in range(0, len(string)-2):
        if (string[i] == string[i + 1]) and (string[i] == string[i + 2]):
            i_0 = i
            i_1 = i + 2
            while (string[i_1] == string[i_0]) and (i_1 < len(string)-1):
                i_1 += 1
            if (string[i_1] == string[i_0]):
                return [i_0, i_1 + 1]
            else:
                return [i_0, i_1]
    return False

# Удаляет лишние символы в строке
def remove_characters(string):
    i = 0
    while i in range(0, len(string)):
        if in_the_array(string[i]) == False:
            string = string.replace(string[i], '')
        i += 1
    i = 0
    while repetition(string):
        string = string.replace(string[repetition(string)[0]:repetition(string)[1]], string[repetition(string)[0]])
    return string

# Ищет слоово в массиве
def find_word(words_list, word):
    for i in range(0, len(words_list)):
        if words_list[i] == word:
            return i
    return -1

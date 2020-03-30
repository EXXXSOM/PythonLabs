#Напишите скрипт, который читает текстовый файл и
#выводит символы в порядке убывания частоты встречаемости
#в тексте. Регистр символа не имеет значения. Программа
#должна учитывать только буквенные символы (символы
#пунктуации, цифры и служебные символы слудет игнорировать).
#Проверьте работу скрипта на нескольких файлах с текстом на
#английском и русском языках, сравните результаты с таблицами,
#приведенными в wikipedia.org/wiki/Letter_frequencies.

import string

russian_w = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
filename = open('Lorem_en.txt')
#filename = open('Lorem_ru.txt')

text = filename.read()
text = text.lower()
print(len(text))

words_count_en = {string.ascii_lowercase[i]: text.count(string.ascii_lowercase[i]) for i in range(len(string.ascii_lowercase))}
words_count_ru = {russian_w[i]: text.count(russian_w[i]) for i in range(len(russian_w))}

print( sorted(words_count_en.items(), key=lambda x: x[1], reverse=True) )
print( sorted(words_count_ru.items(), key=lambda x: x[1], reverse=True) )

#+++
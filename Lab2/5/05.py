#Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все
#слова, которые начинаются с большого латинского символа (от A до Z) и заканчиваются
#2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002».
#Используйте регулярные выражения.
import re

#text = input("Введите текст: ")
text = 'Petr93 Johnny70 Service2002 slaker Test999999999 slaker92'
pattern = r'[A-Z]\D+\d{2,4}\b'

list_words = re.findall(pattern, text)

for i in range(len(list_words)):
    print(list_words[i])

#+++
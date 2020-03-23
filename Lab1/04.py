#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова
#и выводит сначала те слова, длина которых превосходит 7 символов, затем
#слова размером от 4 до 7 символов, затем – все остальные.


def script_split(text):

    words=text.split()

    for i in range (len(words)):
        if len(words[i]) > 7:
            more_7.append(words[i])
        elif len(words[i]) > 4 and len(words[i])< 7:
            between_4and7.append(words[i])
        else:
            less_4.append(words[i])

text = "Текст для работы скриптишка"

more_7 = []
between_4and7 = []
less_4 = []

script_split(text)

print(more_7)
print(between_4and7)
print(less_4)


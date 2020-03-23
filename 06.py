#Напишите программу, позволяющую ввести с клавиатуры
#текст предложения и вывести на консоль все символы,
#которые входят в этот текст ровно по одному разу.

text = input("Введите текст, в котором найдутся все уникальные символы: ")

def count_char (text):
    lower_text = text.lower()
    char = list(lower_text)

    for i in range (len(char)):
        if char.count(char[i]) == 1:
            print(char[i], end = '')

count_char(text)

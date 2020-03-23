#Напишите скрипт, который преобразует введенное с клавиатуры вещественное число в денежный формат.
#Например, число 12.5 должно быть преобразовано к виду «12 руб. 50 коп.».
#В случае ввода отрицательного числа выдайте сообщение «Некорректный формат!» путем обработки исключения в коде.

print("Введите деньги:")

inputMoney = float(input())
def duration_string(inputMoney):
        if inputMoney < 0.0:
                raise
        else:
                return'{} руб. {} коп. '.format(int(inputMoney), int((inputMoney-int(inputMoney))*100))
try:
        print(duration_string(inputMoney))
except:
        print('«Некорректный формат!»')


#Напишите скрипт, позволяющий определить надежность вводимого
#пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.
#https://habrahabr.ru/sandbox/27520/


password = input("Введите ваш пароль: ")

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
 '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
  '[', ']', '^', '_', '`', '{', '|', '}']

numsymbols = 0
upper = 0
countNum = 0
countSym = 0
countUpp = 0
numeric = 0

crash_pass=list(password)
pwlength = len(password)

for i in range (len(crash_pass)):
    if crash_pass[i].isdigit():
        countNum +=1
    if crash_pass[i].isupper():
        countUpp+=1
    for j in range (len(symbols)):
        if crash_pass[i]==symbols[j]:
            countSym+=1

numeric = countNum
numsymbols = countSym
upper = countUpp

pwstrength = ((pwlength * 10)-20 ) + (numeric * 10) + (numsymbols * 15) + (upper * 10)
if pwstrength > 100:   
    pwstrength = 100
elif pwstrength<0:
    pwstrength = 0 

print("Ваш пароль сложен на: " + str(pwstrength))

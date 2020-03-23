#Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000.
#Скрипт должен создать массив из n целых чисел, также сгенерированных случайным
#образом, и дополнить массив нулями до размера, равного ближайшей сверху степени
#двойки. Например, если в массиве было n=100 элементов, то массив нужно дополнить
#28 нулями, чтобы в итоге был массив из 28=128 элементов (ближайшая степень двойки
#к 100 – это число 128, к 35 – это 64 и т.д.).

import random

n = random.randint(1, 100)
arr = []

for i in range(0, n):
    arr.append(random.randint(0, 100))
print(len(arr))
print(arr)

for i in range(n**2):
    if(2**i) > n:
        up = (2**i) - n
        break
    down = (2**i) - n

if (up - n) < (n - down):
    sideSmooth = up
else:
    sideSmooth = down


for i in range(sideSmooth):
    arr.append(0)
print(len(arr))
print(arr)
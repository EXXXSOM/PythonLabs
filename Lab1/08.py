#Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000.
#Скрипт должен создать массив из n целых чисел, также сгенерированных случайным
#образом, и дополнить массив нулями до размера, равного ближайшей сверху степени
#двойки. Например, если в массиве было n=100 элементов, то массив нужно дополнить
#28 нулями, чтобы в итоге был массив из 28=128 элементов (ближайшая степень двойки
#к 100 – это число 128, к 35 – это 64 и т.д.).

from math import log, ceil
import random

random_number = random.randint(1, 10000)

ganarated_array = [random.randint(1, 10) for i in range(random_number)]
print("Начальный массив: ", len(ganarated_array))

[ganarated_array.append(0)
for i in range(pow(2, ceil(log(random_number, 2))) - len(ganarated_array))]
print("Исправленный массив: ", len(ganarated_array))
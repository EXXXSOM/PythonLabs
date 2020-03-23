#Написать скрипт, который выводит на экран «True», если
#элементы программно задаваемого списка представляют
#собой возрастающую последовательность, иначе – «False».

firstList = [1, 2, 3, 4, 5]
secondList = [1, 2, 1, 4, 1]

def check(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return "False - не возрастает."
    return "True - возрастает."

print("--------------")
print(check(firstList))
print(check(secondList))
print("--------------")

#Напишите параметризированный декоратор pre_process, который осуществляет предварительную
#обработку (цифровую фильтрацию) списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а
#можно задать в коде (по умолчанию равен 0.97). Пример кода:
#@pre_process(a=0.93)
#def plot_signal(s):
#    for sample in s:
#        print(sample)

def pre_process(a = 0.97):
    def deckor(func):
        def wrapper():
 
            for i in range(len(s)):
                s[i] = s[i] - a * s[i - 1]
        return wrapper
    return deckor

@pre_process(a = 0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plot_signal(data)

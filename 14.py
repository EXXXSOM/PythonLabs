#Напишите декоратор non_empty, который дополнительно проверяет
#списковый результат любой функции: если в нем содержатся пустые
#строки или значение None, то они удаляются. Пример кода:
#@non_empty
#def get_pages():
#return ['chapter1', '', 'contents', '', 'line1']

def non_empty(funk):
    def wrapper():
        res = funk()
        count = 0
        for i in res:
            if i == '' or i == None:
                res.pop(count)
            count += 1
        return res
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())

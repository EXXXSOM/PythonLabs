#Напишите скрипт, позволяющий искать в заданной директории и в
#ее подпапках файлы-дубликаты на основе сравнения контрольных
#сумм (MD5). Файлы могут иметь одинаковое содержимое, но
#отличаться именами. Скрипт должен вывести группы имен
#обнаруженных файлов-дубликатов.
import os
import hashlib

def path_check(check_path, dictionary):
  for name in os.listdir(check_path):
    path = os.path.join(check_path, name)
    
    if os.path.isfile(path):
      filename = open(path, 'r')
      text = filename.read().encode('utf-8')

      md5 = hashlib.md5(text).hexdigest()
      
      if md5 in sum_dict:
        sum_dict[md5] += [path]
      else:
        sum_dict[md5] = [path]

      filename.close()
    else:
      path_check(path,  dictionary)

  return dictionary

sum_dict = {}
path_check(os.getcwd(), sum_dict)
sum_dict = {sum: group for sum, group in sum_dict.items() if len(group) > 1}

print("Файлы-дубликаты:")
for group in sum_dict.values():
    for path in group:
        print(path)

#+



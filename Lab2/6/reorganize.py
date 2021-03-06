#Напишите скрипт reorganize.py, который в директории --source создает две директории: Archive и Small.
#В первую директорию помещаются файлы с датой изменения, отличающейся от текущей даты на количество
#дней более параметра --days (т.е. относительно старые файлы). Во вторую – все файлы размером меньше
#параметра --size байт. Каждая директория должна создаваться только в случае, если найден хотя бы один
#файл, который должен быть в нее помещен. Пример вызова:
#reorganize --source "C:\TestDir" --days 2 --size 4096
import os
import datetime
import shutil
import argparse

#Команда: "python reorganize.py --source "DirFiles" --days 2 --size 4096"      Чтобы увидеть разницу, нужно ввести --days 6000 (слишком старые файлы)

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', required='True')
parser.add_argument('-si', '--size', type=int)
parser.add_argument('-d', '--days', type=int)

parsed = parser.parse_args()
dir_name = parsed.source
time_dir = os.path.join(dir_name, 'Small')
size_dir = os.path.join(dir_name, 'Archive')
days = parsed.days
size = parsed.size

term = datetime.timedelta(days)
cur_time = datetime.datetime.today()

dir_cache = os.listdir(dir_name) #Если listdir вставить в цикл, то будет считывать некоторые созданные файлы в цикле
for name in dir_cache:
    path = os.path.join(dir_name, name)

    if os.path.getsize(path) < size and os.path.isfile(path):
        if not os.path.exists(time_dir):            
            os.makedirs(time_dir)
            print("Папки нет. Создаем папку: " + time_dir)
        shutil.copy(path, os.path.join(time_dir, os.path.basename(name)))

    creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    if creation_time + term >= cur_time and os.path.isfile(path):
        if not os.path.exists(size_dir):
            os.makedirs(size_dir)
            print("Папки нет. Создаем папку: " + size_dir)
        shutil.copy(path, os.path.join(size_dir, os.path.basename(name)))
        
print("Выполнено!")


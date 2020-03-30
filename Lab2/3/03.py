#Задан путь к директории с музыкальными файлами
#(в названии которых нет номеров, а только названия песен)
#и текстовый файл, хранящий полный список песен с номерами
#и названиями в виде строк формата «01. Freefall [6:12]».
#Напишите скрипт, который корректирует имена файлов в директории
#на основе текста списка песен.

import os
import re

music_list = {}
path_directory = os.getcwd() + "\\Music"
pattern_number = r'(\d+\.\s)[\w\s-]+'
pattern_name = r'\d+\.\s([\w\s-]+)'

f = open (r'MusicList.txt')
lines = f.readlines()
f.close()

for line in lines:
    name =''.join(re.findall(pattern_name, line)).rstrip()
    num = ''.join(re.findall(pattern_number, line))
    music_list[name] = num
    
for name in os.listdir(path_directory):
    if name.endswith('.mp3') and name[:-4] in music_list:
        os.rename(path_directory + "\\" + name, path_directory + "\\" + music_list[name[:-4]] + name)
        
#+++

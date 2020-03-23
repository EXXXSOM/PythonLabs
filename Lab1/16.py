#Напишите скрипт, который на основе списка из 16 названий
#футбольных команд случайным образом формирует 4 группы по 4
#команды, а также выводит на консоль календарь всех игр (игры
#должны проходить по средам, раз в 2 недели, начиная с 14 сентября
#текущего года). Даты игр необходимо выводить в формате «14/09/2016,
#22:45». Используйте модули random и itertools.

import random
import itertools
import datetime
from math import log, ceil

commands = ["Динамо","Спартак","Днепр","Динамо-2",
"ЦСКА","Зенит","Краснодар","Арсенал","Рубин",
"Урал","Енисей","Локомотив","Ростов",
"Уфа","Ахмат","Оренбург",
]

groups = []
for i in range(4):
    groups.append([])
    for j in range(4):
        k = random.randint(
            0, len(commands) - 1
        )
        groups[i].append(commands.pop(k))
date = datetime.datetime(
    datetime.datetime.today().year, 9, 14, random.randint(0, 23), random.randint(0, 59)
)
while date.weekday() != 2:
    date += datetime.timedelta(days=1)
date_s = date

for group in groups:
    print("Группа : " + str(group))
    games = itertools.permutations(group, 2)
    for game in games:
        date = datetime.datetime(
            date.year,
            date.month,
            date.day,
            random.randint(0, 23),
            random.randint(0, 59),
        )
        print( str(game[0]) + " против " + str(game[1]) + " : " + date.strftime("%d/%m/%Y, %H:%M"))
        date += datetime.timedelta(days=14)
    date = date_s 
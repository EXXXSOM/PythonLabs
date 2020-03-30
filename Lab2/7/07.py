#Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома
#(попурри из коротких фрагментов mp3-файлов в пользовательской директории).
#Для манипуляций со звуковыми файлами можно использовать сторонние утилиты, например, FFmpeg.
#Пример вызова и работы скрипта: trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e --- processing file 1: 01 - Intro.mp3 --- processing file 2: 02 - Outro.mp3 --- done!

import os
import subprocess
import argparse
import glob
import random
import sys

import os

#Команда: "python 07.py -d "music_mix" --source "album" --count 3 --frame 10 -l -e"

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--source', required='True')
        parser.add_argument('-d', '--destination')
        parser.add_argument('-c', '--count')
        parser.add_argument('-f', '--frame', default='10')
        parser.add_argument('-l', '--log', action='store_true')
        parser.add_argument('-e', '--extended', action='store_true')

        parsed = parser.parse_args()

        if parsed.destination is None:
            if not os.path.exists(parsed.source + "\\mixs\\mix.mp3"):
                parsed.destination = os.path.join(parsed.source + "\\mixs\\", 'mix.mp3')
            else:
                print('[ВНИМАНИЕ!!!]')
                print('Название микса по стандарту уже существует, повторите команду и укажите новое имя! -d "YouName"')
                exit(0)
        else:
            if not os.path.exists(parsed.source + "\\mixs\\" + parsed.destination + ".mp3"):
                parsed.destination = os.path.join(parsed.source + "\\mixs\\", parsed.destination + ".mp3")
            else:
                print('[ВНИМАНИЕ!!!]')
                print('Такое название микса уже существует, повторите команду и дайте новое название! -d "YouName"')
                exit(0)

        tracklist = list(glob.glob(os.path.join(parsed.source, '*.mp3')))
        if parsed.count is None:
            parsed.count = len(tracklist)

        FNULL = open(os.devnull, 'w')
        parts = []
        for track_num in range(int(parsed.count)):
            each_track = tracklist[track_num]
            track_name = os.path.basename(each_track)
            if parsed.log:
                print('--- processing file {}: {}'.format(
                    track_num + 1, track_name
                ))

            temporary_name = 'part' + str(track_num) + '.mp3'
            start_sec = str(random.randint(30, 60))
            subprocess.call(['ffmpeg\\bin\\ffmpeg.exe', '-ss', start_sec, '-t',
                             str(parsed.frame), '-i', each_track,
                             '-acodec', 'copy', temporary_name],
                            stdout=FNULL, stderr=subprocess.STDOUT)
            final_temporary_name = 'final_' + temporary_name
            if parsed.extended:
                out = str(int(parsed.frame) - 2)
                fade_line = 'afade=t=in:ss=0:d=2,afade=t=out:st=' \
                            + out + ':d=2'
                subprocess.call(['ffmpeg\\bin\\ffmpeg.exe', '-i', temporary_name,
                                 '-af', fade_line, final_temporary_name],
                                stdout=FNULL, stderr=subprocess.STDOUT)
                os.remove(temporary_name)
            else:
                os.rename(temporary_name, final_temporary_name)

            parts += [final_temporary_name]

        concat_line = 'concat:' + '|'.join(parts)
        subprocess.call(['ffmpeg\\bin\\ffmpeg.exe', '-i', concat_line,
                         '-acodec', 'copy', parsed.destination],
                        stdout=FNULL, stderr=subprocess.STDOUT)

        #Удаляем вспомогательные файлы
        for part in parts:
            os.remove(part)

        print("Выполнено!")
    except:
        print('Ошибка!')

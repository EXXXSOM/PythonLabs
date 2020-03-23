#Напишите генератор get_frames(), который производит «оконную
#декомпозицию» сигнала: на основе входного списка генерирует набор
#списков – перекрывающихся отдельных фрагментов сигнала размера
#size со степенью перекрытия overlap. Пример вызова:
#for frame in get_frames(signal, size=1024, overlap=0.5):
#print(frame)

signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_frames(signal, size, overlap):
    size = size * overlap
    start = 0
    end = int(size)

    while end<=len(signal):
        frame = signal[start:end]
        yield frame
        start += int(size)
        end += int(size)
        
for frame in get_frames (signal, size = 10, overlap = 0.5):
    print (frame)

#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова
#и выводит сначала те слова, длина которых превосходит 7 символов, затем
#слова размером от 4 до 7 символов, затем – все остальные.

text = (input("\nВведите текст, который будет разбит на слова: ").split())

more_7 = [word for word in text if len(word) > 7]
between_4and7 = [word for word in text if 4 <= len(word) <= 7]
less_4 = [word for word in text if len(word) < 4]

print("Слова длинной > 7: " , *more_7)
print("Слова длинной <= 7 и >= 4:" , *between_4and7)
print("Остальные слова: " , *less_4)


#Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения
#купюр разного достоинства в заданном количестве. При вводе пользователем запрашиваемой
#суммы денег, скрипт должен вывести на консоль количество купюр подходящего достоинства.
#Если имеющихся денег не хватает, то необходимо напечатать сообщение «Операция не может
#быть выполнена!». Например, при сумме 5370 рублей на консоль должно быть выведено
#«5*1000 + 3*100 + 1*50 + 2*10». 

needMoney = int(input("Введите сумму которую хотите снять: "))

cashBank = dict([(1000, 4), (500, 5), (100, 6), (50, 7), (10, 7)])
outArray = dict()
outInfo = ""

for i in cashBank.keys():

    if needMoney < i:
        continue

    rest = needMoney % i 
    summ = needMoney - rest
    countMoneyCard = summ / i
    if  cashBank[i] >= countMoneyCard: 
        outArray[i] = countMoneyCard
        needMoney = needMoney - summ
    else:
        countMoneyCardRest = countMoneyCard - cashBank[i]
        outArray[i] = cashBank[i] #2
        needMoney = needMoney - (cashBank[i] * i)

    if  needMoney == 0:
        break

if  needMoney == 0:
    print("Выдаем деньги следующими купюрами: ")
    bFirst = True
    for y in outArray.keys():
        if bFirst == True:
            bFirst = False
            outInfo += str(y) + " * " + str("%.0f" % outArray[y])
        else:
            outInfo += " + " + str(y) + " * " + str("%.0f" % outArray[y])
    print(outInfo)
else:
    print("Операция не может быть выполнена!")

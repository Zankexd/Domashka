# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def Boom(Listik=[]):
    trash=[]
    for_return=[]
    for x in Listik:
        if Listik.count(x)>1:
            trash.append(x)
    for x in Listik:
        if x not in trash:
            for_return.append(x)
    print(for_return)


listus=[1,1,3,4,5,5,6,6]
Boom(listus)


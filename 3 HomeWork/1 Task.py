# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
def SumariList(listik=[]):
    sum=0
    quest = listik[1:len(listik):2]
    for x in quest:
        sum+=x
    return quest,sum


list=[1,2,3,4,5]
print(SumariList(list))

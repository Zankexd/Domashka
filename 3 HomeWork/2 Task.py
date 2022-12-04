# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]




list=[1,2,3,4,5,2]
def Joke(list=[]):
    for_return=[]
    if len(list)%2!=0:
        for x in range(0,int(len(list)/2)+1):
            for_return.append(list[x]*list[(-x)-1])
    else:
        for x in range(0,int(len(list)/2)):
            for_return.append(list[x]*list[(-x)-1])

    return for_return

print(Joke(list))

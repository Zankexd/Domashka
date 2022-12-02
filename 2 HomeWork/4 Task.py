# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
Key=int(input())
List=[]
for x in range(-Key,Key+1):
    List.append(x)
print(List)
Found=input()
sum=1
for x in range(0,len(Found),2):
    sum*=(List[int(Found[x])])
print(sum)
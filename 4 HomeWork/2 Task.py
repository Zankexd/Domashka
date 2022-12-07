# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def simple():
    number=int(input())
    listik=[]
    d=2
    while number!=1:
        if number%d==0:
            listik.append(d)
            number=number//d
            d=2
        else:
            d+=1
            if d%2==0:
                d+=1
    print(listik)
simple()
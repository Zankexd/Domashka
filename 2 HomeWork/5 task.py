# Реализуйте алгоритм перемешивания списка.
import random

ara=[]
k=0
for x in range(-5,6):
    ara.append(x)
print(ara)
for x in range(0,random.randint(0,len(ara)+1)):
    randomchik=random.randint(0,len(ara)+1)
    k=ara[randomchik]
    ara[randomchik]=ara[x]
    ara[x]=k
print(ara)
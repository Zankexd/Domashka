# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11
f=0
Key=input()
for x in range(2,len(Key)):
    f+=int(Key[x])
print(f)
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
week=int(input("please type number 1-7"))
if week<=5 and week>0:
    print(week,"No")
if week<=7 and week>5:
    print(week,"Yes")

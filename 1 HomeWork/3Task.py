# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка. ⋀ - and ⋁ - or ¬ - not
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
X=int(input("Write x ="))
Y=int(input("Write y ="))

if X<0 and Y<0:
    print("3")
if X>0 and Y<0:
    print("4")
if X<0 and Y>0:
    print("2")
if X>0 and Y>0:
    print("1")
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

wow=int(input("Write 1-4 ="))
if wow==1:
    print("X>0 and Y>0")
if wow==2:
    print("X<0 and Y>0")
if wow==3:
    print("X<0 and Y<0")
if wow==4:
    print("X>0 and Y<0")
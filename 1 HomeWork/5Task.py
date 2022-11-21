# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
A=int(input("A first dot"))
A1=int(input("A second dot"))
B=int(input("B first dot"))
B1=int(input("B second dot"))
print(round((((A1-A)**2)+((B1-B)**2))**.5,3))
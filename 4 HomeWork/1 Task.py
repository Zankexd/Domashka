# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#
#     Ввод: 0.001
#     Вывод: 3.141
import math

def Pi():
    N=input()
    print(round(math.pi,len(N)-2))

Pi()
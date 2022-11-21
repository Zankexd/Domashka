# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#⋀ - and ⋁ - or ¬ - not
print(" ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
X=int(input("Write 1=True 0=False for X ="))
Y=int(input("Write 1=True 0=False for Y ="))
Z=int(input("Write 1=True 0=False for Z ="))

print(not(X or Y or Z)== (not X and not Y and not Z))


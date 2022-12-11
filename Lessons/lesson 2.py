# def math (op,x,y):
#     print(op(x,y))
# f=lambda x,y: x+y
# math(f,10,10)
# list=[x for x in range(1,100) if x!=10]
# print(list)
List=None
List2=[]
with open("lesson2.txt","r")as file:
    List=file.readline()
List2=List.split()

f=lambda x: x**3
List3=[(f(int(x)),int(x))for x in List2 if int(x)%2==0]
print(List3)
# Создайте программу для игры в ""Крестики-нолики"".
wins=[[1,2,3],[1,5,9],[1,4,7],[3,6,9],[4,5,6],[3,5,7],[7,8,6]]
f=[
    ["|",1,"|",2,"|",3,"|"],
    ["------------"],
    ["|",4,"|",5,"|",6,"|"],
    ["------------"],
    ["|",7,"|",8,"|",9,"|"]
]
def table(p):
    for x in p:
        print(*x)
table(f)
def Changes(t,symbol,place):
    for y in range(0,5,2):
        for x in range(1,6,2):
            if t[y][x]==place:
                t[y].pop(x)
                t[y].insert(x,symbol)
    return t

def Champ(p1,p2,wins):
    for x in wins:
        list=[i for i in x if i in p1]
        if len(list)==3:
            print("first player 1  win")
            return False
        list = [i for i in x if i in p2]
        if len(list) == 3:
            print("first player 2  win")
            return False
def Steps(t):
    cucold=1
    p1_list = []
    p2_list = []
    while cucold==1:
        p1=int(input("position_x="))

        table(Changes(t,"X",p1))
        p1_list.append(p1)
        if len(p1_list) or len(p2_list) >=2:
            if 0 == Champ(p1_list, p2_list, wins):
                break
        p2 = int(input("position_o="))
        table(Changes(t,"0",p2))
        p2_list.append(p2)
        if len(p1_list) or len(p2_list) >=2:
            if 0 == Champ(p1_list, p2_list, wins):
                break
    return 0

def main():

    while returkis:
        if Steps(f)==0:
            break






main()

# Champ([3,2,1,4],[1,2,3],wins)

# Changes(f,"x",5)
# table(f)
# print([1,2,3]  [3,2,1])
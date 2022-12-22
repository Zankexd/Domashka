def add(Data):
    name = input("Введите имя человека")
    second_name = input("Введите фамилию человека")
    number = input("Введите номер человека")
    with open(Data,"a") as file:
        file.writelines(f"{name}\n")
        file.writelines(f"{second_name}\n")
        file.writelines(f"{number}\n\n")

def deleted(Data):
    name=input("Введите имя человека которого нужно удалить")
    data_base=None
    with open(Data,"r") as file:
        data_base=file.read()
    data_base=data_base.split()
    listik=[x for x in range(0,len(data_base)) if data_base[x]==name]

    for x in listik:
        quw=input(f"{data_base[x]} {data_base[x+1]} {data_base[x+2]}. Это тот человек?")
        if quw=="Нет" or quw=="нет":
            continue
        if quw=="Да" or quw=="да":
            data_base.pop(x)
            data_base.pop(x + 1)
            data_base.pop(x + 2)
    with open(Data,"w") as file:
        for x in data_base:
            if x.isdigit():
                file.writelines(f"{x}\n\n")
            else:
                file.writelines(f"{x}\n")
    return data_base

def find(data):
    data_base = None
    with open(data, "r") as file:
        data_base = file.read()
    data_base = data_base.split()
    func=input('1-поиск по имени 2-по фамилии 3-по номеру телефона')
    match func:
        case "1":
            name = input('введите ')
            listik = [x for x in range(0, len(data_base)) if data_base[x] == name]
            for x in listik:
                quw = input(f"{data_base[x]} {data_base[x + 1]} {data_base[x + 2]}. Это тот человек?")
                if quw == "Нет" or quw == "нет":
                    continue
                if quw == "Да" or quw == "да":
                    print(f"{data_base[x]} {data_base[x + 1]} {data_base[x + 2]}.")
        case "2":
            name = input('введите ')
            listik = [x for x in range(0, len(data_base)) if data_base[x] == name]
            for x in listik:
                quw = input(f"{data_base[x-1]} {data_base[x]} {data_base[x + 1]}. Это тот человек?")
                if quw == "Нет" or quw == "нет":
                    continue
                if quw == "Да" or quw == "да":
                    print(f"{data_base[x-1]} {data_base[x]} {data_base[x + 1]}.")
        case "3":
            name = input('введите ')
            listik = [x for x in range(0, len(data_base)) if data_base[x] == name]
            for x in listik:
                quw = input(f"{data_base[x - 2]} {data_base[x - 1]} {data_base[x]}. Это тот человек?")
                if quw == "Нет" or quw == "нет":
                    continue
                if quw == "Да" or quw == "да":
                    print(f"{data_base[x - 2]} {data_base[x - 1]} {data_base[x]}.")
def view(data):
    for_view=None
    with open(data,"r") as file:
        for_view=file.read()
    print(for_view)

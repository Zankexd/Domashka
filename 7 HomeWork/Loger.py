import datetime


def Log(func):
    name=input("Введите ваше для логирования данных")
    match func:
        case "1":
            with open("Log.txt","a") as file:
                file.writelines(f"Создал базу даных-{name} время-{datetime.datetime.now()}\n")
        case "2":
            with open("Log.txt", "a") as file:
                file.writelines(f"Искал человека в базе данных-{name} время-{datetime.datetime.now()}\n")
        case "3":
            with open("Log.txt", "a") as file:
                file.writelines(f"Удалил человека в базе данных-{name} время-{datetime.datetime.now()}\n")
        case "4":
            with open("Log.txt", "a") as file:
                file.writelines(f"Добавил человека в базу данных-{name} время-{datetime.datetime.now()}\n")
        case "5":
             with open("Log.txt","a") as file:
                file.writelines(f"Посмотрел базу данных-{name} время-{datetime.datetime.now()}\n")
        case "6":
             with open("Log.txt", "a") as file:
                file.writelines(f"Посмотрел лог-{name} время-{datetime.datetime.now()}\n")



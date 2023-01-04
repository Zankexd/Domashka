import Edit
import Fill_data
import seek
import Loger

def Controler(Data="Data.txt"):
    Flag=True
    while Flag:
        num_func=input("Выберите желаемую функцию:\n 1-создать базу данных\n 2-Найти человека в базе данных\
        \n 3-Удалить человека из базы\n 4-Добавить человека в базу\n 5-Посмотреть базу\n 6-Посмотреть лог \n 7-завершить работу")
        Loger.Log(num_func)
        match num_func:
            case "1":
                Fill_data.create_and_fill_data()
                print("Создана база данных")
            case "2":
                seek.find(Data)
            case "3":
                Edit.deleted(Data)
                print("Операция завершина")
            case "4":
                Edit.add(Data)
                print("Операция завершина")
            case "5":
                seek.view(Data)
            case "6":

                seek.view("log.txt")
            case "7":
                Flag = False



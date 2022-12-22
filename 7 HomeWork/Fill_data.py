import random

def create_and_fill_data(count=10):
    name=["Алексей","Владислав","Александр","Богдан","Андрей","Николай","Максим","Иван","София","Виталина","Карина",\
          "Марина","Мария","Оливия","Анджела","Богдана","Наруто"]

    second_name=["Кудесник","Фантомас","Крыжовник","Фукус","Узумаки","Петрунык","Лошадь"]
    File="Data.txt"
    with open(File,"w") as file:
        for x in range(0,count):
            file.writelines(f"{name[random.randint(0,len(name)-1)]}\n")
            file.writelines(f"{second_name[random.randint(0,len(second_name)-1)]}\n")
            file.writelines(f"{str(random.randint(1000000000,99999999999))}\n\n")
    return File
def update(Data,text):
    with open(Data,"w") as file:
        file.writelines(text)


# class Person:
#     def __init__(self, imya):
#         self.mishurik = imya
#         self.status = "учитель"
#
#     def __str__(self):
#         return f"бравл старс:{self.mishurik} {self.status}"
#     def common_method(self):
#         print("сан-ди-ля-ва-.ХЭ-ХЭЙ-ВАКА-ВАКА-ХЭЙ-ХЭЙ")
#
# chelovek = Person("ы")
#
# print(chelovek.mishurik)
# print(chelovek)
# print(chelovek.common_method())

# class Iaga:
#     def __init__(self, tetya, surnam, ag):
#         self.name = tetya
#         self.surname = surnam
#         self.age = ag
#
#     def __str__(self):
#         return f"имя:{self.name},\nфамилия:{self.surname},\nвозраст:{self.age}\n"
#
#     def greet(self):
#         return f"привет!меня зовут {self.surname} {self.surname} и мне {self.age} лет"
#
#
# tank = Iaga("Margarita", "Egorovna", 40)
# print(tank.name, tank.surname, tank.age)
# print(tank)
# print(tank.greet())

# import random
class Iaga:
    def __init__(self, tetya, surnam, ag):
        self.name = tetya
        self.surname = surnam
        self.age = ag

    def __str__(self):
        return f"имя:{self.name},\nфамилия:{self.surname},\nвозраст:{self.age}\n"

    def greet(self):
        return f"привет!меня зовут {self.surname} {self.surname} и мне {self.age} лет"


tank = Iaga("Margarita", "Egorovna", 40)
print(tank.name, tank.surname, tank.age)
print(tank)
print(tank.greet())
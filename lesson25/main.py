# class Human:
#     statik = "новосибирск"
#
#     def __init__(self, rost=1, ves=100):
#         self.height = rost
#         self.jir = ves
#
#     def public(self):
#         pass
#
#     def __private(self):
#         pass
#
#
# peson = Human(47)
# print(peson.height)
# print(peson.jir)
from random import randint


class Human:
    default_name = "Антон"
    default_age = 33

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return (self.name, self.age, self.__money, self.__house)

    def earn_money(self):
        self.__money += 75000

    def default_info(self):
        return (self.default_age, self.default_name)

    def __make_deal(self, dom):
        if self.__money >=  dom.final_price():
            self.__money -=  dom.final_price()
            return  True

    def buy_house(self, dom):
        if self.__make_deal(dom):
             dom.owner = self.name
             self.__house = dom

class House:
    def __init__(self, ar, pr):
        self.__area = ar
        self.__price = pr
        self.skidka = randint(5, 25) / 100

    def final_price(self):
        return self.__price - (self.__price * (randint(5, 25) / 100))


artem = Human()
dom1 = House("Новосиб", 1000000)
print(dom1.final_price())
print(artem.buy_house(dom1))

# class mashina:
#     def __init__(self, wheel: int, doors: int, pdk: bool):
#         self.wheels = wheel
#         self.doors = doors
#         self.pdk = pdk
#         self.__probeg = 10000
#
#     def go_ot(self):
#         if self.pdk:
#             self.pdk = False
#             return "дядя коля изгнан"
#         else:
#             return "кайфуем"
#
#     def __obnuiyai(self):
#         self.__probeg = 0
#
#     def selling(self):
#         self.__obnuiyai()
#
#
# nissan = mashina(wheel=8, doors=8, pdk=True)
# print(nissan.go_ot())
#
# print(nissan.pdk)
# nissan.pdk = True
#
# # print(nissan.__probeg)
# nissan.__probeg = 500
# import string
#
#
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.__lang = "eng"
#         self.__letters = string.ascii_lowercase
#
#     def print(self):
#         return self.__letters
#
#     def nums_kolvo(self):
#         return len(self.__letters)
#
#
# alpha = Alphabet("eng", "abcdefghijklmnopqrstuvwxyz")
# print(alpha.print())
# print(alpha.nums_kolvo())
#
# class Car:
#     def __init__(self, color: str, type: str, year: int):
#         self.color = color
#         self.color = type
#         self.color = year
#
#     def zapusk(self):
#         return "заведен"
#
#     def zaglush(self):
#         return "заглушен"
#
import datetime


class Chasi:
    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)

    def addH(self):
        self.__h += 1

    def addM(self):
        self.__m += 1

    def addS(self):
        self.__s += 1

    def vivod(self):
        return f"{self.__h}:{self.__m}:{str(self.__s).rjust(2,'0')}"


luboe = Chasi()
luboe.addH()
print(luboe.vivod())

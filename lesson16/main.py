# x = 10
# y = 5
# l1 = lambda x, y:x + y +1
# print(l1(x, y))

# answer = "д"
# result = lambda is_exit: True if is_exit == "д" else False
# print(result(answer))

# l = []
# for i in range(1, 5 + 1):
#     l.append(i)
# print(l)
# l2 = [i for i in range(1, 6)]
# print(l2)

# c2f = lambda c: 9/5 * c + 32
# print(c2f(100))
#
# f2c = lambda f: 5/9 * (f - 32)
# print(f2c(82))
#
# c2k = lambda k: k - 273.15
# print(c2k(800))
#
# k2c = lambda k: k - 273.15
# print(k2c(450))
#
# f2k = lambda f: c2k(f2c(203))
# print(f2c(203))

# from random import randint
# exit = lambda answer: True if answer == "д" else False
# while True:
#     skolko = int(input("сколько???:"))
#     dice = [randint(1,6) for i in range(skolko)]
#     print(dice)
#     answer = input("хотите выйти?? д/н")
#     if exit(answer):
#         break
# from random import choice
# slovar = {}
# user = "https://github.com"
# slovar = {user:"qwerty"}
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")]
# vseshestsimvolov = [choice(choice(chars))for i in range(6)]
# code = ''.join(vseshestsimvolov)
# print(code)
# if user in slovar:
#     print("ссылка используется",slovar[user])
# else:
#     slovar[user] = code
#     print("добавлено",code)

# import math
# a = 5
# b = 2
# otvet = lambda a, b: b - a
# otvet1 = lambda a, b: b + a
# otvet2 = lambda a, b: b / a
# otvet3 = lambda a, b: b * a
# otvet4 = lambda a, b: a / b
# otvet5 = lambda x: -x if x < 0 else x
# otvet6 = lambda a, b:math.log(b, a)
# print(otvet6(5, 25))

field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]

for row in range(3):

    for column in range(3):
        pass
print(list(field.values()))
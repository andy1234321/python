# try:
#     x = int(input("введи число:"))
#     print(10 / x)
# except (ValueError,ZeroDivisionError):
#     print("лано.....")
# # except ZeroDivisionError:
# #     print("не дели на 0")
# except Exception:
#     pass
# else:
#     print("ы")
# finally:
#     print("я устал")

# x = input("введи имя друга(собаки)")
# try:
#  if x == "Антон":
#     raise NameError("ахахахаахаха,мох👴")
# except NameError as pelmeni:
#     print("низя",pelmeni)
# def skladivanie():
#     s = 0
#     k = 0
#     for number in content:
#         try:
#             s += float(number)
#         except ValueError:
#             print("найдено не число", number)
#         else:
#             k += 1
#         if k == 0:
#             return "не найдено чисел"
#     return round(s / k, 2)
#
# try:
#     f = open("file.txt", "r", encoding="utf - 8")
# except FileNotFoundError:
#     print("филе нет")
#     exit()
# content = f.read().split()
# print(content)
#
# print("ср. арифм =", skladivanie())
try:
    f = open("file.txt", "r", encoding="utf - 8")
except FileNotFoundError:
    print("нет филе")
    exit()
content = f.readlines()
print(content)

for i, student in enumerate(content):
    content[i] = student.split()

print(content)

maxi = -1
imya = ""
familiya = ""
for student in content:
    if int(student[3]) > maxi:
        maxi = int(student[3])
        imya = student[1]
        familiya = student[0]
print(imya, familiya, maxi)

# a = input("a:")
# b = input("b:")
# lst = []
# for abdula in range(a + 1, b):
#     lst.append(abdula ** 2)
#
# print(lst)

# text = input("сообщения:")
# lst = text.split(" ")
# print(lst)
# lst.reverse()
# print(lst)

# number = "0"
# chet = 0
# nechet = 0
# while number != "end":
#     number = input("число: ")
#     if number.lstrip("-").isdigit():
#         number = int(number)
#         lst
#     elif number == "end":
#         break
#     else:
#         print("введи число!")
#         continue
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
# print(f"четных:{chet}шт.")
# print(f"неyчетных:{nechet}шт.")

# a = input("числа:").split(" ")
# for i in range(1, len(a)):
#     if int(a[i]) > int(a[i-1]):
#         print(f"я считаю,что {a[i]} больше,чем {a[i-1]}.")

# lst = [-5,14,2,-8,11]
# maxi = max(lst)
# mini = min(lst)
# lst[lst.index(mini)],lst[lst.index(maxi)] = lst[lst.index(maxi)],lst[lst.index(mini)]
# print(lst)

lst1 = ["lo", "mov"]
lst2 = ["ve", "avi"]

lst3 = []
for i, j in zip(lst1, lst2):
    lst3.append(i + j)
print(lst3)

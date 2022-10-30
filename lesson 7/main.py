# x=15/0(ZeroDivisionError)
# x=15+"a"(TypeError)
# x=[10,5,3]
# print(x[3])(IndexError)
# x="hello world.(SyntaxError)
# x=int("a")(ValueError)

# assert

# def summa(number:list[int]):
#     return  sum(number)
# assert summa([1,3]) == 5(AssertionError)
# assert summa([1,3]) == 4(vse horosho)
# try:
#     x=5/0
# except:
#     print("oshibka")
# try:
#     x=5/0
#     int("x")
# except ZeroDivisionError:
#     print("деление на ноль")
# except Exception:
#     print("я обработаю все")
# try:
#     x = int(input("введи число:"))
# except ValueError:
#     print("э,уважаемый хочу цифры")
# else:
#     print("ура победа ты не глуп")
# finally:
#     print("я отработал")
# try:
#     name = input("ведите имя:")
#     if name == "антон":
#         raise Exception("антона нельзя")
# except Exception as error_messege:
#     print("одна ошибка и ты ошибся🐺")
#     print("ошибка то фатальная",error_messege)
# try:
#     x=5/0
# except ZeroDivisionError:
#     pass
# if 5>3:
#     pass
# temperatura = 50
# print ()
# x / / 5

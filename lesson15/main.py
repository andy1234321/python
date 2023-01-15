# s={"a","divan","ded"}
# print(s)

# def hello_world():
#     print("hello_world")
# hello_world()

# def plus(chislo1:int,chislo2:int) -> int:
#     """
#     :param chislo1:
#     :param chislo2:
#     :return:
#     """
#     answer = chislo1 + chislo2
#     return answer
#
# x = plus(54,88)
# print(x+2)

# def is_sorted(list1):
#     clone_l = sorted(list1)
#     if list1 == clone_l:
#         return True
#
#
# l = [4, 5, 6, 7, 8]
# if is_sorted(l):
#     print("принтанул")
# else:
#     print("не принтанул")

# def find_longest(slova1):
#     shifri = []
#     for i in slova1:
#         shifri.append(len(i))
#     ind228=shifri.index(max(shifri))
#     return slova1[ind228],shifri[ind228]
# slova = ["tank", "minekraft", "egg", "connect", "H2o-sostav"]
# print(find_longest(slova))

def min_max(qwe):
    mini = qwe[0]
    maxi = qwe[0]
    for i in qwe:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
    return mini, maxi


qwe = [4, 3, 5, 6, 7]
print(min_max(qwe))
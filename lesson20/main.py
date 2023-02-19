# # f = open("8 б сегодня дежурный класс.txt", "w", encoding="utf-8")
# # f.write("hello world\n")
# # f.write("привет мир")
# # f.close()
# f = open("8 б сегодня дежурный класс.txt", "r", encoding="utf-8")
# # content = f.read()
# content = f.readlines()
# print(content)
# for line in content:
#     print(line)
# f.close()
# f = open("data.txt", "w", encoding="utf-8")
# while f != " ":
#     f.write(input("напиши че нибудь"))
# f.close()


# name = input("назови:")
# f = open(name + ".txt", "r", encoding="utf-8")
# g = f.readlines()
# n = 0
# for line in g:
#     n = n + 1
#     print(str(n)+") "+line.rstrip())
# f.close()

# f0 = open("data.txt", "r", encoding="utf-8")
# v = f0.readlines()
# f0.close()
# nf = 0
# while not v:
#     nf = nf + 1
#     fm = open(str(nf) + ". txt", "w", encoding="utf-8")
#     ts = v[:3]
#     for line in ts:
#         fm.write(line)
#     del v[:3]
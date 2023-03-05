import json

# open("я геннадий.txt", "w", encoding="utf = 8").write("привки я генадий")
# text = [1, 5.3, True, None, [1, 2], (5, 7), "ENG", "РУС"]
# f = open("я геннадий.json", "w", encoding="utf-8")
# json.dump(text, f, ensure_ascii=False)
# b = json.dumps(text, ensure_ascii=False)
# print(b)
# f.close()

# f = open("я геннадий.json", "r", encoding="utf-8")
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()

# f = open("ягенадий2.txt", "r", encoding="utf-8")
# con = f.readlines()
# print(con)
# f.close()
# dict = {}
#
# for elem in con:
#     print(elem)
#     lomka = elem.split(": ")
#     print(lomka[0])
#     print(lomka[1])
#     dict[lomka[0]] = lomka[1].rstrip("\n")
#
# print(dict)
# ff = f = open("ягенадий2.json", "w", encoding="utf-8")
# json.dump(dict, ff)
# ff.close()

f = open("я геннадий.json", "r", encoding="utf-8")
content = json.load(f)
f.close()
for i,em in enumerate(content):
   if type(em) == str:
        content[i] = content[i] + "!"
print(content)
# phrase = "я всегда я когда я есть я".lower()
# symbols = list ("!.,?")
# phrase_cleared = ""
# for dfg in phrase:
#     if dfg not in symbols:
#         phrase_cleared += dfg
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# d = {}
# for element in l:
#     if element not in d:
#         d[element] = 1
#     else:
#         d[element] += 1
# print(d)

# pokupki = {"чипсы":78,
#            "кириешки":13,
#            "яйца":70,
#            "МЕГА АНТОН":999}
# s = 0
# # for i in pokupki:
# for i in pokupki.values():
#     s += i
# print(s)

phrase = "я всегда я когда я есть я".lower()
symbols = list ("!.,?")
phrase_cleared = ""
for dfg in phrase:
    if dfg not in symbols:
        phrase_cleared += dfg
print(phrase_cleared)
l = phrase_cleared.split(" ")
d = {}
for element in l:
    if element not in d:
        d[element] = 1
    else:
        d[element] += 1
print(d)
maxi = max(d.values())
print(maxi)
for (key,value) in d.items():
    if value == maxi:
        # print(key,value)
        if value == maxi:
            print(f"{key}:{value}")
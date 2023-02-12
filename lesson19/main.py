def alphabet(s):
    return s[::-1]
alphabetmin = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetmax = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
reversbig = alphabet(alphabetmax)
reversemaloi = alphabet(alphabetmin)
message = input("введи че нибудь:")
word = ''
for i in message:
    if i not in alphabetmax and i not in alphabetmin:
        word = word + i
        continue
    if i.isupper():
        ind = alphabetmax.index(i)
        letter = (reversbig[ind])

    else:
        ind = alphabetmin.index(i)
        letter = (reversemaloi[ind])
    word = word + letter
print(word)
input()
cveta = (input())
cveta2 = list(cveta)
perehodi = 0
q = 0
y = 0
while perehodi < len(cveta2) - 1:
    if cveta2[q] == cveta2[q + 1]:
        y += 1
    perehodi += 1
    q += 1
print(y)

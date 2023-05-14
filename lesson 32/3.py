n = int(input())
a = 0
for i in range(n):
    zadacha = input()
    if int(zadacha[0]) + int(zadacha[2]) + int(zadacha[4]) > 1:
        a += 1
print(a)

words = int(input())
for i in range(words):
    words2 = input()
    if len(words2) > 10:
        print(str(words2[0])+str(len(words2) - 2)+str(words2[-1]))
    else:
        print(words2)

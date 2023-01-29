def minusf(f):
    global beans
    beans = beans - f
print("У вас есть куча, состоящая из 20 фасолин. Вы и оппонент, по очереди, берете из нее по 1, 2 или 3 фасолины до тех пор, пока из всей кучи не останется 1 фасолина. Тот, чья очередь будет забирать последнюю фасолину – проиграл.")
beans = 20
while True:

    while True:
        f1 = int(input("1 сколько бобов возьмёшь? 1-3"))
        if f1 > 0 and f1 < 4:
            break
    minusf(f1)
    if beans < 1:
        break
    print(beans)

    while True:
        f2 = int(input("2 сколько бобов возьмёшь? 1-3"))
        if f2 > 0 and f2 < 4:
            break
    minusf(f2)
    if beans < 1:
        break
    print(beans)
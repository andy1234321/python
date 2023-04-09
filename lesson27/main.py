# c1 = input("Введите первый цвет:").lower().strip()
# c2 = input("Введите второй цвет:").lower().strip()
# c = ("красный", "синий", "желтый")
# if (c1 not in c) or (c2 not in c):
#     print("Один из основных цветов введён неверно")
# elif (c1 == c[0] and c2 == c[2]) or (c1 == c[2] and c2 == c[0]):
#     print("оранжевый")
# elif (c1 == c[0] and c2 == c[1]) or (c1 == c[1] and c2 == c[0]):
#     print("зеленый")
# elif (c1 == c[1] and c2 == c[2]) or (c1 == c[2] and c2 == c[1]):
#     print("фиолетовый")
# else:
#     print(c1.capitalize())

nach = input("Начало первого урока (чч:мм):")
dlur = int(input("Начало первого урока (мин):"))
dlp = int(input("Начало первого перемен (мин):"))
n = int(input("На сколько уроков нужно расписание:"))
h, m = nach.split(":")
h, m = int(h), int(m)
time = h * 60 + m
for i in range(n):
    print(f"урок{i + 1}:", end="")
    h = time // 60
    m = time % 60
    print(f"{str(h).rjust(2,'0')}:{str(m).rjust(2,'0')} - ", end="")
    time = time + dlur
    h = time // 60
    m = time % 60
    print(f"{str(h).rjust(2,'0')}:{str(m).rjust(2,'0')} - ", end="")
    time = time + dlp

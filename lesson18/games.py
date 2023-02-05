import easygui as ez
import random


def rock_paper_scissors():
    k = "k.png"
    c = "c.png"
    a = "a.png"
    vtm = random.choice([k, c, a])
    x = ez.buttonbox(title="камень ножницы бумага",
                     msg="выбери что нибудь",
                     images=[k, c, a],
                     choices=("выход отсюда",)
                     )
    if x == "выход отсюда":
        return
    else:
        if x == c and vtm == c:
            ez.msgbox(msg="ничья")
        elif x == a and vtm == a:
            ez.msgbox(msg="ничья")
        elif x == k and vtm == k:
            ez.msgbox(msg="ничья")
        elif x == k and vtm == a:
            ez.msgbox(msg="проигрыш")
        elif x == k and vtm == c:
            ez.msgbox(msg="выигрыш")
        elif x == c and vtm == k:
            ez.msgbox(msg="проигрыш")
        elif x == c and vtm == a:
            ez.msgbox(msg="выигрыш")
        elif x == a and vtm == k:
            ez.msgbox(msg="выигрыш")
        else:
            ez.msgbox(msg="проигрыш")


def guess_the_number():
    a = random.randint(1, 100)
    m = ez.integerbox(
        msg='Попробуй отгадать число',
        title='От 1 до 100',
        lowerbound=1,
        upperbound=100,
    )
while a != m:
    if m > a:
        m = ez.integerbox(
            msg=f'число меньше{m}',
            title='От 1 до 100',
            lowerbound=1,
            upperbound=100,
            image="many.png"
        )

        if m < a:
            m = ez.integerbox(
                msg=f'число больше{m}',
                title='От 1 до 100',
                lowerbound=1,
                upperbound=100,
                image="more.png"
            )


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = ez.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()

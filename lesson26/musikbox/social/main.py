from user import User

u1 = User("Смирнов", "Антон", "smir-ant", 12345)
u2 = User()
print(u1.imya)
print(u2.imya)
users = [u1, u2]
i = input("логин:")
p = input("пароль:")
for u in users:
    if u.log_in()in(i, p):
        print("ты вошел")
        current_user = u


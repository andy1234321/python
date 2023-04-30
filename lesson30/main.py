from tkinter import *
from random import randint
from tkinter import messagebox

win = Tk()
win.geometry("500x500")


# def get_lst(pelmeni):
#     indxs = lstbox.curselection()
#     for ind in indxs:
#         print(lst[ind])
#
#
# lst = ["один", "два", "три"]
# lstbox = Listbox(win, selectmode=EXTENDED, bg="green", fg="white", selectbackground="pink",
#                  selectforeground="white", selectborderwidth=20)
# lstbox.pack()
#
# # Button(win, text="кнопка", command=get_lst).pack()
# lstbox.bind("<<ListboxSelect>>", get_lst)
#
# # for elem in lst:
# #     lstbox.insert(END, elem)
#
# lst_tk = StringVar(value=lst)
# lstbox['listvariable'] = lst_tk
# messagebox.showinfo("инфа", "оооочень важная")
# messagebox.showerror()
# messagebox.showwarning()
# Button(win, text="на чиле на расслабоне", bg="darkgreen").pack(anchor=W, fill=BOTH, expand=True)
# Button(win, text="text").pack(pady=5, ipadx=11)
# Button(win, text="toze text").pack(pady=5)
# Button(win, text="батон").grid(column=0, row=0)
# Button(win, text="еще батон").grid(column=1, row=0)
# Button(win, text="тоже батон").grid(column=2, row=0, rowspan=2, sticky=NS)
# Button(win, text="и опять батон").grid(column=0, row=1, columnspan=2, sticky=EW)
# Button(win, text="батон").place(x=500, y=500)
# def hello():
#     print("приффки")
#     win.after(1000, hello)
#
#
# win.after(2000, hello())
# def hello(e):
#     print("приффки")
# btn = Button(win, text="кнопка")
# btn.pack()
# btn.focus_set()
# btn.bind("<Return>", hello)
# btn.bind("<h>", hello)
# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)
# print(rb_val.get())
# Entry(win, show="*").pack()  # создаст Entry где любые символы отобразятся как *
# Entry(win, show="Э").pack()  # да, любые вводимые символы отобразятся как Э
# lab = Label(win, text="логин:")
# lab.grid(column=0, row=0)
# ent = Entry(win)
# ent.grid(column=1, row=0)
# lab1 = Label(win, text="логин:")
# lab1.grid(column=0, row=1, pady=5)
# ent1 = Entry(win)
# ent1.grid(column=1, row=1, pady=5)
# btn = Button(win, text="Авторизация")
# btn.grid(column=1, row=3, sticky=E, pady=5)
def hello(da):
    x = randint(0, 400)
    y = randint(0, 400)
    btn.place(x=x, y=y)


x = 10
y = 10
btn = Button(win, text="поймай меня")
btn.place(x=x, y=y)
btn.bind("<Enter>", hello)

win.mainloop()

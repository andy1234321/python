from tkinter import *

win = Tk()
win.geometry("500x500")


# def click_rbm(event):
#     ent.get()
#     lab['text'] = ent.get()
#
#
# win = Tk()
# win.geometry("100x100")
#
# lab = Label(win, text="////")
# lab.pack()
#
# ent = Entry(win)
# ent.bind("<Button-3>", click_rbm)
# ent.pack(
# def izmen():
#     if rb_val.get() == 1:
#         lab["text"] = start + " " + rb["text"]
#     else:
#         lab["text"] = start + " " + rb1["text"]
#
#
# rb_val = IntVar()
# start = "hello"
# lab = Label(win, text=start + "....", font="Arial 15 normal")
# lab.pack()
# rb = Radiobutton(win, text="Arkasha", font="Arial 15 normal", variable=rb_val, value=1, command=izmen)
# rb.pack()
# rb1 = Radiobutton(win, text="Vitalik", font="Arial 15 normal", variable=rb_val, value=2, command=izmen)
# rb1.pack()
# def get_cb():
#     print(cb_val.get())
#     if cb_val.get() == True:
#         btn['state'] = "normal"
#
#
# cb_val = BooleanVar()
# cb = Checkbutton(text="активировать",
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False,
#                  command=get_cb)
def get_scala(val):
    print(scala.get())
    print(val)
    if scala.get():
    win['bg'] = colors[scala.get()]

scala = Scale(win, from_=0, to=5,
              orient="horizontal",
              length=300,
              command=get_scala)
scala.pack
win.mainloop()

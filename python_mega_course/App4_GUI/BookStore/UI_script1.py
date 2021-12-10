from tkinter import *

window = Tk()


def km_to_miles():

    t1_text = str(int(e1_value.get()) * 1000)
    t1.insert(END, chars=t1_text)

    t2_text = str(int(e1_value.get()) * 2.20642)
    t2.insert(END, chars=t2_text)

    t3_text = str(int(e1_value.get()) * 35.274)
    t3.insert(END, chars=t3_text)


b1 = Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)


t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()

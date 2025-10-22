from tkinter import *
window = Tk()
window.title('Calculator')
window.geometry('700x400')

num1 = IntVar()
num2 = IntVar()

def sum():
    add = num1.get() + num2.get()
    result1.config(text=f'Sum is {add}')

def diff():
    diff = num1.get() - num2.get()
    result1.config(text=f'Difference is {diff}')
  
def mul():
    mul = num1.get() * num2.get()
    result1.config(text=f'Multiplication is {mul}')

def div():
    if num2.get() == 0:
        result1.config(text="ERROR", fg='red')
    else:
        div = num1.get() / num2.get()
        result1.config(text=f'Division is {div}', fg='green')

def mod():
    if num2.get() == 0:
        result1.config(text="ERROR", fg='red')
    else:
        mod = num1.get() % num2.get()
        result1.config(text=f'Modulus is {mod}', fg='green')
        
title = Label(window, text='Calculator', font=('Times new Roman', 20), fg='red')
title.place(x=270, y=60)

l1 = Label(window, text='Number1:', font=('Times new Roman', 20))
l1.place(x=100, y=120)

tb1 = Entry(window, textvariable=num1, font=('Times new Roman', 20))
tb1.place(x=220, y=120)

l2 = Label(window, text='Number2:', font=('Times new Roman', 20))
l2.place(x=100, y=180)

tb2 = Entry(window, textvariable=num2, font=('Times new Roman', 20))
tb2.place(x=220, y=180)

bt1 = Button(window, text='+', command=sum, font=('Times new Roman', 20))
bt1.place(x=50, y=250)

bt2 = Button(window, text='-', command=diff, font=('Times new Roman', 20))
bt2.place(x=150, y=250)

bt3 = Button(window, text='*', command=mul, font=('Times new Roman', 20))
bt3.place(x=250, y=250)

bt4 = Button(window, text='/', command=div, font=('Times new Roman', 20))
bt4.place(x=350, y=250)

bt5 = Button(window, text='%', command=mod, font=('Times new Roman', 20))
bt5.place(x=450, y=250)

result1 = Label(window, text=' ', font=('Times new Roman', 20))
result1.place(x=220, y=300)

window.mainloop()


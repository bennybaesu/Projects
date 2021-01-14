# SIMPLE CALCULATOR PROGRAM
# AUTHOR: Benjamin Baesu

import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.geometry("400x650")

a = ''
b = ''


def test():
    print("Test")


T = tk.Text(root, height=11, width=11)
T.grid(row=1, column=0)


def appendNumber(num):
    T.insert(tk.END, num)


photo0 = tk.PhotoImage(file=r"Images/button0.gif").subsample(11, 11)
photo1 = tk.PhotoImage(file=r"Images/button1.gif").subsample(11, 11)
photo2 = tk.PhotoImage(file=r"Images/button2.gif").subsample(11, 11)
photo3 = tk.PhotoImage(file=r"Images/button3.gif").subsample(11, 11)
photo4 = tk.PhotoImage(file=r"Images/button4.gif").subsample(11, 11)
photo5 = tk.PhotoImage(file=r"Images/button5.gif").subsample(11, 11)
photo6 = tk.PhotoImage(file=r"Images/button6.gif").subsample(11, 11)
photo7 = tk.PhotoImage(file=r"Images/button7.gif").subsample(11, 11)
photo8 = tk.PhotoImage(file=r"Images/button8.gif").subsample(11, 11)
photo9 = tk.PhotoImage(file=r"Images/button9.gif").subsample(11, 11)
photoAC = tk.PhotoImage(file=r"Images/buttonAC.gif").subsample(11, 11)
photoNegative = tk.PhotoImage(file=r"Images/buttonNegative.gif").subsample(11, 11)
photoDivide = tk.PhotoImage(file=r"Images/buttonDivide.gif").subsample(11, 11)
photoPercent = tk.PhotoImage(file=r"Images/buttonPercent.gif").subsample(11, 11)
photoMultiply = tk.PhotoImage(file=r"Images/buttonMultiply.gif").subsample(11, 11)
photoSubtract = tk.PhotoImage(file=r"Images/buttonSubtract.gif").subsample(11, 11)
photoAdd = tk.PhotoImage(file=r"Images/buttonAdd.gif").subsample(11, 11)
photoEqual = tk.PhotoImage(file=r"Images/buttonEqual.gif").subsample(11, 11)
photoDot = tk.PhotoImage(file=r"Images/buttonDot.gif").subsample(11, 11)

button0 = tk.Button(
    image=photo0,
    command=lambda: appendNumber('0'))
button1 = tk.Button(
    image=photo1,
    command=test)
button2 = tk.Button(
    image=photo2,
    command=test)
button3 = tk.Button(
    image=photo3,
    command=test)
button4 = tk.Button(
    image=photo4,
    command=test)
button5 = tk.Button(
    image=photo5,
    command=test)
button6 = tk.Button(
    image=photo6,
    command=test)
button7 = tk.Button(
    image=photo7,
    command=test)
button8 = tk.Button(
    image=photo8,
    command=test)
button9 = tk.Button(
    image=photo9,
    command=test)
buttonAC = tk.Button(
    image=photoAC,
    command=test)
buttonNegative = tk.Button(
    image=photoNegative,
    command=test)
buttonDivide = tk.Button(
    image=photoDivide,
    command=test)
buttonPercent = tk.Button(
    image=photoPercent,
    command=test)
buttonMultiply = tk.Button(
    image=photoMultiply,
    command=test)
buttonSubtract = tk.Button(
    image=photoSubtract,
    command=test)
buttonAdd = tk.Button(
    image=photoAdd,
    command=test)
buttonEqual = tk.Button(
    image=photoEqual,
    command=test)
buttonDot = tk.Button(
    image=photoDot,
    command=test)

button0.grid(row=6, column=0)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonAC.grid(row=2, column=0)
buttonNegative.grid(row=2, column=1)
buttonDivide.grid(row=2, column=3)
buttonPercent.grid(row=2, column=2)
buttonMultiply.grid(row=3, column=3)
buttonSubtract.grid(row=4, column=3)
buttonAdd.grid(row=5, column=3)
buttonEqual.grid(row=6, column=3)
buttonDot.grid(row=6, column=2)

root.mainloop()

# -*- coding: utf-8 -*-

from Tkinter import *

def Quit():
    root.destroy()

root = Tk()
root.title("PyServer")
root.resizable(False, False)
frame0 = Frame(root, width=200, height=200)
frame0.grid(row=0, column=0, columnspan=1)
frame = Frame(root, width=200, height=200)
frame.grid(row=0, column=1, columnspan=1)

logbox = Text(frame0,width=50, font='Arial 10',wrap=WORD)
#logbox.grid(row=0, column=0, rowspan = 5)
scr = Scrollbar(frame0)
scr.config(command=logbox.yview)
logbox.config(yscrollcommand=scr.set)
scr.pack(side="right", fill="y", expand=False)
logbox.pack(side="left", fill="both", expand=True)

massL = Label(frame, text="Mass wto fuel (kg):", width=15)
massL.grid(row=0, column=1, rowspan = 1)
massE = Entry(frame, width=10)
massE.grid(row=0, column=2, rowspan = 1)

fmL = Label(frame, text="Fuel mass (kg):", width=15)
fmL.grid(row=1, column=1, rowspan = 1)
fmE = Entry(frame, width=10)
fmE.grid(row=1, column=2, rowspan = 1)

dmfsL = Label(frame, text="ΔmFuel/s (kg):", width=15)
dmfsL.grid(row=2, column=1, rowspan = 1)
dmfsE = Entry(frame, width=10)
dmfsE.grid(row=2, column=2, rowspan = 1)

egvL = Label(frame, text="E.G.V. (m/s):", width=15)
egvL.grid(row=3, column=1, rowspan = 1)
egvE = Entry(frame, width=10)
egvE.grid(row=3, column=2, rowspan = 1)

gravL = Label(frame, text="Gravity (m/s^2):", width=15)
gravL.grid(row=4, column=1, rowspan = 1)
gravE = Entry(frame, width=10)
gravE.grid(row=4, column=2, rowspan = 1)

buttonGen = Button(frame, text="Generate", width=20, height=1)
buttonGen.grid(row=5, column=1, columnspan = 2)

buttonWrite = Button(frame, text="Write file", width=20, height=1)
buttonWrite.grid(row=6, column=1, columnspan = 2)

buttonQuit = Button(frame, text="Quit", width=20, height=1,
                 command=Quit)
buttonQuit.grid(row=7, column=1, columnspan = 2)

root.mainloop()
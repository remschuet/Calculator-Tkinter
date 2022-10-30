from tkinter import *


Quiz = Tk()
Quiz.geometry("557x678")
Quiz.configure(background='pink')
Quiz.title("Vérité ou Action")

List = ""

def Press(num):
    global List

    List = List + str(num)

    equation.set(List)

def PressEqual():
    global List
    total = str(eval(List))
    equation.set(total)

    List = ""

def Clear():
    global List
    List = ""
    equation.set("")

equation = StringVar()
expression_field = Entry(Quiz, textvariable=equation)
expression_field.pack()
expression_field.place(x=0, y=615, height=60, width=557)

# Bouton pour le niveau ami
ButtonNum1 = Button(Quiz, text="1",
                    height=4,
                    width=8,
                    command=lambda: Press(1),
                    font=('Helvetica', '20'))
ButtonNum1.pack()
ButtonNum1.place(x=0, y=0)

# Bouton pour le niveau intermédiaire
ButtonNum2 = Button(Quiz, text="2",
                    height=4,
                    width=8,
                    command=lambda: Press(2),
                    font=('Helvetica', '20'))
ButtonNum2.pack()
ButtonNum2.place(x=140, y=0)

# Bouton pour le niveau hard
ButtonNum3 = Button(Quiz, text="3",
                    height=4,
                    width=8,
                    command=lambda: Press(3),
                    font=('Helvetica', '20'))
ButtonNum3.pack()
ButtonNum3.place(x=280, y=0)

ButtonNumMulti = Button(Quiz, text="X",
                    height=4,
                    width=8,
                    command=lambda: Press("*"),
                    font=('Helvetica', '20'))
ButtonNumMulti.pack()
ButtonNumMulti.place(x=420, y=0)

# Bouton pour le niveau extreme
ButtonNum4 = Button(Quiz, text="4",
                    height=4,
                    width=8,
                    command=lambda: Press(4),
                    font=('Helvetica', '20'))
ButtonNum4.pack()
ButtonNum4.place(x=0, y=154)

ButtonNum5 = Button(Quiz, text="5",
                    height=4,
                    width=8,
                    command=lambda: Press(5),
                    font=('Helvetica', '20'))
ButtonNum5.pack()
ButtonNum5.place(x=140, y=154)

ButtonNum6 = Button(Quiz, text="6",
                    height=4,
                    width=8,
                    command=lambda: Press(6),
                    font=('Helvetica', '20'))
ButtonNum6.pack()
ButtonNum6.place(x=280, y=154)

ButtonNumDiv = Button(Quiz, text="/",
                    height=4,
                    width=8,
                    command=lambda: Press("/"),
                    font=('Helvetica', '20'))
ButtonNumDiv.pack()
ButtonNumDiv.place(x=420, y=154)

ButtonNum7 = Button(Quiz, text="7",
                    height=4,
                    width=8,
                    command=lambda: Press(7),
                    font=('Helvetica', '20'))
ButtonNum7.pack()
ButtonNum7.place(x=0, y=308)

ButtonNum8 = Button(Quiz, text="8",
                    height=4,
                    width=8,
                    command=lambda: Press(8),
                    font=('Helvetica', '20'))
ButtonNum8.pack()
ButtonNum8.place(x=140, y=308)

ButtonNum9 = Button(Quiz, text="9",
                    height=4,
                    width=8,
                    command=lambda: Press(9),
                    font=('Helvetica', '20'))
ButtonNum9.pack()
ButtonNum9.place(x=280, y=308)

ButtonNumSoust = Button(Quiz, text="-",
                    height=4,
                    width=8,
                    command=lambda: Press("-"),
                    font=('Helvetica', '20'))
ButtonNumSoust.pack()
ButtonNumSoust.place(x=420, y=308)

ButtonNum0 = Button(Quiz, text="0",
                    height=4,
                    width=8,
                    command=lambda: Press(0),
                    font=('Helvetica', '20'))
ButtonNum0.pack()
ButtonNum0.place(x=0, y=462)

ButtonNumPoint = Button(Quiz, text=".",
                    height=4,
                    width=8,
                    command=lambda: Press("."),
                    font=('Helvetica', '20'))
ButtonNumPoint.pack()
ButtonNumPoint.place(x=140, y=462)

ButtonNumTotal = Button(Quiz, text="=",
                    height=4,
                    width=8,
                    command=PressEqual,
                    font=('Helvetica', '20'))
ButtonNumTotal.pack()
ButtonNumTotal.place(x=280, y=462)

ButtonNumAdd = Button(Quiz, text="+",
                    height=4,
                    width=8,
                    command=lambda: Press("+"),
                    font=('Helvetica', '20'))
ButtonNumAdd.pack()
ButtonNumAdd.place(x=420, y=462)

Quiz.mainloop()
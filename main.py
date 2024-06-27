from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="lightblue")

input_entry = Entry(width=40)
equation = ""

class Functions:

    def clear():
        global equation
        equation = ""
        input_entry.delete(0, END)

    def append_to_equation(char):
        global equation
        equation += str(char)
        input_entry.delete(0, END)
        input_entry.insert(0, equation)

    def solve():
        global equation
        equation = str(eval(equation))
        input_entry.delete(0, END)
        input_entry.insert(0, equation)

button_0 = Button(root, text="0", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(0))
button_1 = Button(root, text="1", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(1))
button_2 = Button(root, text="2", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(2))
button_3 = Button(root, text="3", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(3))
button_4 = Button(root, text="4", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(4))
button_5 = Button(root, text="5", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(5))
button_6 = Button(root, text="6", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(6))
button_7 = Button(root, text="7", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(7))
button_8 = Button(root, text="8", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(8))
button_9 = Button(root, text="9", width=9, height=4, font=("Unispace", 8), command=lambda: Functions.append_to_equation(9))

button_solve = Button(root, text="=", font=("Unispace", 8), width=9, height=4, command=Functions.solve)

button_add = Button(root, text="+", font=("Unispace", 8), width=9, height=4, command=lambda: Functions.append_to_equation("+"))
button_subtract = Button(root, text="-", font=("Unispace", 8), width=9, height=4, command=lambda: Functions.append_to_equation("-"))
button_multiply = Button(root, text="x", font=("Unispace", 8), width=9, height=4, command=lambda: Functions.append_to_equation("x"))
button_divide = Button(root, text="/", font=("Unispace", 8), width=9, height=4, command=lambda: Functions.append_to_equation("/"))
button_clear = Button(root, text="CE", width=9, height=4, font=("Unispace", 8), command=Functions.clear)

input_entry.grid(row=0, column=0, columnspan=4, pady=6, padx=6)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_clear.grid(row=4, column=0)
button_solve.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
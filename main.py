from tkinter import *
from tkinter import messagebox, Text

window = Tk()  # Initialization the tkinter

window.title("Calculator")  # Setting title
window.minsize(width=500, height=500)  # Setting width and height
#window.maxsize(width=500, height=500)

# Declare label
lblHeading = Label(text="Welcome to calculator program", font=("Arial", 10, "bold"))
#lblHeading.pack(side="left")
lblHeading.pack()

lblFirstNo = Label(text="Enter first number")
lblFirstNo.pack()
lblFirstNo.place(x=65, y=20)

lblSecondNo = Label(text="Enter second number")
lblSecondNo.pack()
lblSecondNo.place(x=46, y=52)

lblResult = Label(text="Result: ")
lblResult.pack()
lblResult.place(x=128, y=82)

lblOutput = Label(text="")
lblOutput.pack()
lblOutput.place(x=165, y=82)

txtFirst = Entry(width=20)
txtFirst.pack()
txtSecond = Entry(width=20)
txtSecond.pack(padx=10, pady=10)


def add_click():
    try:
        # Get values from the textboxes
        first_value = float(txtFirst.get())
        second_value = float(txtSecond.get())

        # Add the values
        result = first_value + second_value

        # Display the result in lblResult
        lblOutput.config(text=f" {result}")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers")


def sub_click():
    try:
        # Get values from the textboxes
        first_value = float(txtFirst.get())
        second_value = float(txtSecond.get())

        # Add the values
        result = first_value - second_value

        # Display the result in lblResult
        lblOutput.config(text=f" {result}")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers")


def mul_click():
    try:
        # Get values from the textboxes
        first_value = float(txtFirst.get())
        second_value = float(txtSecond.get())

        # Add the values
        result = first_value * second_value

        # Display the result in lblResult
        lblOutput.config(text=f" {result}")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers")


def div_click():
    try:
        # Get values from the textboxes
        first_value = float(txtFirst.get())
        second_value = float(txtSecond.get())

        # Add the values
        result = first_value / second_value

        # Display the result in lblResult
        lblOutput.config(text=f" {result}")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers")
def clear_click():
    try:
        txtFirst.delete(0, 'end')
        txtSecond.delete(0, 'end')

        # Display the result in lblResult
        lblOutput.config(text="")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Declare button
frame = Frame(window)
frame.pack()

btnAdd = Button(frame, text="Add", command=add_click)
btnAdd.grid(row=2, column=1, padx=5, pady=5)

btnSub = Button(frame, text="Sub", command=sub_click)
btnSub.grid(row=2, column=2, padx=5, pady=5)

btnMul = Button(frame, text="Mul", command=mul_click)
btnMul.grid(row=3, column=1, padx=5, pady=5)

btnDiv = Button(frame, text="Div", command=div_click)
btnDiv.grid(row=3, column=2, padx=5, pady=5)
btnClear = Button(frame, text="Clear", command=clear_click)
btnClear.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()  # Display UI. This line will end of the program

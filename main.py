from tkinter import *

window = Tk()  # Initialization the tkinter

window.title("Calculator")  # Setting title
window.minsize(width=500, height=300)  # Setting width and height

# Declare label
lblHeading = Label(text="Welcome to calculator program", font=("Arial", 20, "bold"))
lblHeading.pack(side="left")

# Declare button
btnAdd=Button(text="Add")
btnAdd.pack()

window.mainloop()  # Display UI. This line will end of the program

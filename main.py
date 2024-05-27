import tkinter

window = tkinter.Tk() # Initialization the tkinter

window.title("Calculator") # Setting title
window.minsize(width=500, height=300) # Setting width and height

# Declare label
lblHeading = tkinter.Label(text="Welcome to calculator program", font=("Arial",20, "bold"))
lblHeading.pack(side="left")

import turtle
tim = turtle.Turtle()
tim.write("Hell Santosh")



window.mainloop() # Display UI. This line will end of the program

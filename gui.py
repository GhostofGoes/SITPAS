#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

# GUI: Graphical User Interface
# tkinter is a Python "wrapper" around Tcl/Tk GUI framework.
#
# To run a basic demo and test if it's working
# on your system, run the following command:
#   python -m tkinter

# create a root widget
root = Tk()

# set the window title
root.title("SITPAS")

# Background color
root.configure(background="blue")

# Smallest size it can be
root.minsize(500, 500)  # width, height

# Largest size it can be
root.maxsize(1000, 1000)

# Where the window starts on the screen
root.geometry("300x300+50+50")  # width x height + x + y

# There are several ways to place stuff in the GUI
# .pack() : relative to other items, auto-decided by Tk
# .grid() : more precise

# Create some text labels
Label(root, text="What's your label").pack()
# label_1.pack()
label_2 = Label(root, text="this is a label too")
label_2.pack()

# add a image file
image = PhotoImage(file="labtocat.png", height=300, width=300)
image.zoom(2)
img = Label(root, image=image)  # images are associated with labels
img.pack()

def killProgram():
    root.destroy()

# Add a button to exit the program
frm = ttk.Frame(root, padding=10)
frm.pack()
Label(frm, text="Hello World!").pack()
Button(frm, text="Quit", command=killProgram).pack()

# start the gui
root.mainloop()

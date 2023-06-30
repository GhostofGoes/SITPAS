#!/usr/bin/env python3

# from tkinter import *

# root = Tk()
# root.mainloop()


from tkinter import *

root = Tk()  # create a root widget
root.title("Tk Title")  # Window title
root.configure(background="blue")  # Background color
# Smallest size it can be
root.minsize(800, 800)  # width, height
# Largest size it can be
# root.maxsize(500, 500)
# Where the window starts on the screen
root.geometry("300x300+50+50")  # width x height + x + y



# root = Tk()
# root.title("Tk Example")
# root.minsize(200, 200)  # width, height
# root.geometry("300x300+50+50")

# Create Label in our window
text = Label(root, text="What's your label")
text.pack()
text2 = Label(root, text="this is a label too")
text2.pack()

# Create Label in our window
image = PhotoImage(file="labtocat.png")
image.zoom(2)
img = Label(root, image=image)
img.pack()

# start the gui
root.mainloop()

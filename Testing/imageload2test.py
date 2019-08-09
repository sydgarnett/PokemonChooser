#!/usr/bin/env python3
import sys
from tkinter import Tk, Label, PhotoImage
root = Tk()
# First command line arg is image path. PNG format
img = PhotoImage(file="APC/250px-722.gif")
my_image = Label(root,image=img)
my_image.pack()

root.mainloop()
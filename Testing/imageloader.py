#!/usr/bin/env python3
from tkinter import *

# Putting a gif image on a canvas with Tkinter
# tested with Python24 by  vegaseat  25jun2005
# create the canvas, size in pixels
canvas = Canvas(width = 250, height = 250)
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = 'APC/250px-722.gif')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0,3, image = gif1, anchor = NW)
# run it ...
mainloop()
#!/usr/bin/env python3

from tkinter import *

#creating the window
root= Tk()
#modify root window
root.title("Labeler")
root.geometry("200x50")

app=Frame(root)
app.grid()
# label=Label(app,text="this is a label")
# label.grid()

button1=Button(app,text="this is a button")
button1.grid()

button2=Button(app)
button2.grid()
button2.configure(text="this will show text")

button3= Button(app)
button3.grid()
button3["text"]="This will show up as well"
#kick off the event loop
root.mainloop()
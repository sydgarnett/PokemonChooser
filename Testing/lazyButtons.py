#!/usr/bin/env python3
from tkinter import *

class Application(Frame):
    """a GUI application with 3 buttons"""
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.buttonClicks=0
        self.createWidgets()
    def createWidgets(self):
        self.button=Button(self)
        self.button["text"]="total Clicks: 0"
        self.button["command"]=self.updateCount
        self.button.grid()
    def updateCount(self):
        self.buttonClicks+=1
        self.button["text"]="total Clicks: "+str(self.buttonClicks)
        # self.button1=Button(self,text="this is a button")
        # self.button1.grid()
        # 
        # self.button2=Button(self)
        # self.button2.grid()
        # self.button2.configure(text="this will show text")
        # 
        # self.button3= Button(self)
        # self.button3.grid()
        # self.button3["text"]="This will show up as well"
        
root=Tk()
root.title("lazyButtons")
root.geometry("200x85")

app=Application(root)
root.mainloop()
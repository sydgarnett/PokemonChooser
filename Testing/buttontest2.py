#!/usr/bin/env python3

from tkinter import *

class Application(Frame):
    """a GUI application with 3 buttons"""
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.instruction= Label(self,text= "enter the password")
        self.instruction.grid(row=0,column=0,columnspan=2,sticky=W)
        
        self.password=Entry(self)
        self.password.grid(row=1,column=1,sticky=W)
        
        self.submitButton=Button(self,text="Submit",command=self.reveal)
        self.submitButton.grid(row=2,column=0,sticky=W)
        
        self.text=Text(self,width=35,height=5,wrap=WORD)
        self.text.grid(row=3,column=0,columnspan=2,sticky=W)
    def reveal(self):
        """display message based on the password typed in"""
        content=self.password.get()
        if content=="password":
            message="You have access to something special."
        else:
            message="Access Denied."
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
root=Tk()
root.title("Password")
root.geometry("250x150")
app=Application(root)

root.mainloop()
    
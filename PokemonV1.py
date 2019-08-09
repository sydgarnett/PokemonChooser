#!/usr/bin/env python3
from tkinter import *
import creator
import creator2
import creator3
file=open("APC/PokemonListAllNames.txt","r")
line=file.readlines()

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        #instructions and submit button
        self.instruction1= Label(self,text= "Welcome To the Pokemon Chooser! Once you finish click either button.")
        self.instruction1.grid(row=0,column=0,columnspan=2,sticky=N)
        self.submitButton=Button(self,text="1st Pokemon",command=self.reveal)
        self.submitButton.grid(row=0,column=3,sticky=W)
        self.submit2Button=Button(self,text="2nd Pokemon",command=self.reveal2)
        self.submit2Button.grid(row=0,column=4,sticky=W)
        self.submit3Button=Button(self,text="3rd Pokemon",command=self.reveal3)
        self.submit3Button.grid(row=1,column=3,sticky=W)
        #entry widgets
        self.dayEnt=Entry(self)
        self.dayEnt.grid(row=1,column=0,sticky=N)
        self.instructionD= Label(self,text= "Day")
        self.instructionD.grid(row=1,column=1,sticky=W)
        
        self.monthEnt=Entry(self)
        self.monthEnt.grid(row=2,column=0,sticky=N)
        self.instructionM= Label(self,text= "Month")
        self.instructionM.grid(row=2,column=1,sticky=W)
        
        self.yearEnt=Entry(self)
        self.yearEnt.grid(row=3,column=0,sticky=N)
        self.instructionD= Label(self,text= "Year")
        self.instructionD.grid(row=3,column=1,sticky=W)
        
        self.nameEnt=Entry(self)
        self.nameEnt.grid(row=5,column=0,sticky=N)
        self.instructionN= Label(self,text= "First Name & Last Name")
        self.instructionN.grid(row=5,column=1,sticky=W)
        
        self.instructionV=Label(self,text="Ver.1.2")
        self.instructionV.grid(row=7,column=0,sticky=W)
        
        #Text box in case of error? or for more info
        self.text=Text(self,width=27,height=15,wrap=WORD)
        self.text.grid(row=6,column=0,columnspan=2,sticky=W)
        #for images
        #Drop down menu (to switch between versions perhaps)
        #need to figure out how to get images on here
        self.img = PhotoImage(file="APC/250px-Pokeball.gif")
        self.my_image = Label(self,image=self.img)
        self.my_image.grid(row=6,column=1,sticky=W)
    def reveal(self):
        try:
            content=eval(self.dayEnt.get())
            content2=eval(self.monthEnt.get())
            content3=eval(self.yearEnt.get())
            contentName=(self.nameEnt.get())
            if isinstance(content,int) and isinstance(content2,int) and isinstance(content3,int) and content3<100:
                revealer=creator.Creator(content,content2,content3,contentName)
                message=revealer.getFirstName()+" "+revealer.getLastName()+"\nYour 1st Pokemon Is #"+str(revealer.FinalNum())+"\nIts name is "+line[revealer.FinalNum()-1]+ "This pokemon is from the "+revealer.region()+"\n"+str(revealer.shinyConfirm())
                if revealer.isShiny():
                    self.img = PhotoImage(file="APC/Shiny/s"+str(revealer.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
                else:
                    self.img = PhotoImage(file="APC/Normal/250px-"+str(revealer.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
            else:
                message="ERROR...Dont use the full year. Use the last 2 digits."
                self.img = PhotoImage(file="APC/Normal/250px-"+str(revealer.FinalNum())+".gif")
                self.my_image = Label(self,image=self.img)
                self.my_image.grid(row=6,column=1,sticky=W)
        except NameError:
            message="ERROR... Use Numbers for Dates. for example 1/1/99."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except SyntaxError:
            message="ERROR...Something's Wrong. Try again.\n(for months use single digits)"
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except ValueError:
            message="ERROR...Use Letters and make sure you use your first and last name."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
    def reveal2(self):
        try:
            content=eval(self.dayEnt.get())
            content2=eval(self.monthEnt.get())
            content3=eval(self.yearEnt.get())
            contentName=(self.nameEnt.get())
            if isinstance(content,int) and isinstance(content2,int) and isinstance(content3,int) and content3<100:
                revealer2=creator2.Creator2(content,content2,content3,contentName)
                message=revealer2.getFirstName()+" "+revealer2.getLastName()+"\nYour 2nd Pokemon Is #"+str(revealer2.FinalNum())+"\nIts name is "+line[revealer2.FinalNum()-1]+"This pokemon is from the "+revealer2.region()+"\n"+str(revealer2.shinyConfirm())
                if revealer2.isShiny():
                    self.img = PhotoImage(file="APC/Shiny/s"+str(revealer2.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
                else:
                    self.img = PhotoImage(file="APC/Normal/250px-"+str(revealer2.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
            else:
                message="ERROR...Dont use the full year. Use the last 2 digits."
                self.img = PhotoImage(file="APC/X_mark.gif")
                self.my_image = Label(self,image=self.img)
                self.my_image.grid(row=6,column=1,sticky=W)
        except NameError:
            message="ERROR... Use Numbers for Dates. for example 1/1/99."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except SyntaxError:
            message="ERROR...Something's Missing. Try again."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except ValueError:
            message="ERROR...Use Letters and make sure you use your first and last name."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
    def reveal3(self):
        try:
            content=eval(self.dayEnt.get())
            content2=eval(self.monthEnt.get())
            content3=eval(self.yearEnt.get())
            contentName=(self.nameEnt.get())
            if isinstance(content,int) and isinstance(content2,int) and isinstance(content3,int) and content3<100:
                revealer3=creator3.Creator3(content,content2,content3,contentName)
                message=revealer3.getFirstName()+" "+revealer3.getLastName()+"\nYour 3rd Pokemon Is #"+str(revealer3.FinalNum())+"\nIts name is "+line[revealer3.FinalNum()-1]+"This pokemon is from the "+revealer3.region()+"\n"+str(revealer3.shinyConfirm())
                if revealer3.isShiny():
                    self.img = PhotoImage(file="APC/Shiny/s"+str(revealer3.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
                else:
                    self.img = PhotoImage(file="APC/Normal/250px-"+str(revealer3.FinalNum())+".gif")
                    self.my_image = Label(self,image=self.img)
                    self.my_image.grid(row=6,column=1,sticky=W)
            else:
                message="ERROR... Use the last 2 digits for the year."
                self.img = PhotoImage(file="APC/X_mark.gif")
                self.my_image = Label(self,image=self.img)
                self.my_image.grid(row=6,column=1,sticky=W)
        except NameError:
            message="ERROR... Use Numbers for Dates. for example 1/1/99."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except SyntaxError:
            message="ERROR...Something's Missing. Try again."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        except ValueError:
            message="ERROR...Use Letters and make sure you use your first and last name."
            self.img = PhotoImage(file="APC/X_mark.gif")
            self.my_image = Label(self,image=self.img)
            self.my_image.grid(row=6,column=1,sticky=W)
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
root=Tk()
root.title("Find your Pokemon!")
root.geometry("700x400")
app=Application(root)

root.mainloop()

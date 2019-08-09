#!/usr/bin/env python3
#Winter Term Project Version1

class Creator2():
    def __init__(self,day,month,year,name):
        self.day=day
        self.month=month
        self.year=year
        self.name=name
    def getFirstName(self):
        space=self.name.index(" ")
        firstName=self.name[0:space]
        return firstName
    def getLastName(self):
        space=self.name.index(" ")
        lastName=self.name[space+1:]
        return lastName
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year
    def countSet(self,name):
        alpha="0ABCDEFGHIJKLMNOPQRSTUVWXYZ0abcdefghijklmnopqrstuvwxyz"
        count=alpha.index(name[0:1])
        return count%27
    def birthTotal(self):
        if self.year<10:
            return self.month+((self.day//10)+(self.day%10))+self.year
        else:
            return self.month+((self.day//10)+(self.day%10))+(self.year/10)
    def decimal(self):
        deci=0.00
        first=self.getFirstName()
        a=self.countSet(first)
        c=a
        deci+=c
        last=self.getLastName()
        b=self.countSet(last)
        d=(float)(b*.1)
        deci+=d;
        return deci;  
    def FinalNum(self):
        FinNum=self.birthTotal()*self.decimal();
        if (FinNum>809.0):
            return round(FinNum%809);
        return round(FinNum);
    def isShiny(self):  
        x=len(self.name)-1
        if(x%10==0):
            x=x//10
            u=self.FinalNum()//10
            d=u%10
            return x==u%10
        o=self.FinalNum()%10
        return x==self.FinalNum()%10
    def shinyConfirm(self):
        if (self.isShiny()==True):
            return "This pokemon is Shiny!"
        return ""
    def region(self):
        if (self.FinalNum()<=151):
            return "Kanto Region"
        elif(self.FinalNum()>=152 and self.FinalNum()<=251):
            return "Johto Region"
        elif(self.FinalNum()>=252 and self.FinalNum()<=386):
            return "Hoenn Region"
        elif(self.FinalNum()>=387 and self.FinalNum()<=493):
            return "Sinnoh Region"
        elif(self.FinalNum()>=494 and self.FinalNum()<=649):
            return "Unova Region"
        elif(self.FinalNum()>=650 and self.FinalNum()<=721):
            return "Kalos Region"
        elif(self.FinalNum()>=722 and self.FinalNum()<=809):
            return "Alola Region"
        return "???"

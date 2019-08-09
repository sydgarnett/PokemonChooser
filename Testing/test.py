#!/usr/bin/env python3
#test
import creator3
day=13
month=9
year=98
name="GydneY Sarnett"

test= creator3.Creator3(day,month,year,name)
print("version 3")
print("Profile:")
print("Name:",test.getFirstName(),test.getLastName())
print("Birthday (D/M/Y):",test.getDay(),"/",test.getMonth(),"/",test.getYear())
print(test.countSet(test.getFirstName()),"firstname count")
print(test.countSet(test.getLastName()),"lastname count")
print(test.decimal(),"decimal")
print(test.birthTotal(),"birthday total")
print(test.FinalNum(),"is your pokemon number.\nIt is from the",test.region())

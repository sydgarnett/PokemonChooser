#!/usr/bin/env python3
#test2
import creator2
day=31
month=12
year=76
name="Zony Zarnet"

test2= creator2.Creator2(day,month,year,name)

print(test2.getFirstName(),test2.getLastName())
print("version 2")
print("birthday is:",test2.getDay(),"/",test2.getMonth(),"/",test2.getYear(),"||d/m/y")
print(test2.countSet(test2.getFirstName()),"firstName count")
print(test2.countSet(test2.getLastName()),"lastName count")
print(test2.decimal(),"decimal")
print(test2.birthTotal(),"birthday total")
print(test2.FinalNum(),"final number")
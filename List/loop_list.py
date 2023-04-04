

#lists are iterable onjeccts.Therefore they can easily be used with 
#for loop

#for name in iterable obj:
  #  print(name) this would print each element from goven iterable obj.

list=["str1","str2",3,4,5,6]
for item in list:
    print(item)

# print only string objects from given list
for element in list:
   if type (element)==str:
       print(f"String objects:{element}")


#print only int objects
for element in list:
   if type (element)==int:
       print(f"Int objects:{element}")
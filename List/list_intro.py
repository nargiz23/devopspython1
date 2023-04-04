
l1=[2,5,True,"str",3.14]

print(type(l1))  #class 'list"
print(l1[2]) # True

#print(l1[10]) # index Error

print(type(l1[4])) # class float

#as we practice in str we can't get range of elements from list

print(l1[2:5]) # [True,"Str",3.14]
#when we getting range of elements from list return will be another list
print(type(l1[2:5])) #class list

#when [2:5] 5 element not included


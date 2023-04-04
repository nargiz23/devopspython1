
#all numerical types in Python are immutable,which means
#they won"t change their value unless reassigned

num=7
print(num)  #7
print(type(num)) #7

print (num /3) # 2.3
print(num) #7
print(type(num)) #<class '>int'

num=10
print("after re-assignment")
print(num)
print(type(num))

#Lets reassign the value num with a different type
print("After assigning with a different data type")
num=10.0
print(num)
print(type(num))

num="A text"
print(num)
print(type(num))


#In pyhon the variable can change their values as well
#as their data types after reassignment

#Let's make this var num a numerical type.

num=10
num+=3#num =num +3
print(num)








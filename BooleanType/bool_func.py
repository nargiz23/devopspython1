
num1=1
num2=0
print(bool(num1))#variable num1 will be converted to boolean
                #therefore it will take the value True
print(bool(num2))#we will get the false because when 0 converted to
                 #boolean we get False

s="" #'' same way they works
print("The boolean value of emthy string is",bool(s))

list =[]
print("The boolean value of emthy list is",bool(list))

tuple=()
print("The boolean value of emthy list is",bool(tuple))

#q1:
print(bool("False"))
#only empty str gives False output
print(len("Py "))
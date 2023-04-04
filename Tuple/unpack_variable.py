

#Unpacking is assigning element of a seguence,such as tuple or
#a list,to seperate variables

elements=("word","python",12,13)
#we could unpack this tuple
var1,var2,var3,var4=elements
print(var1) # word
print(var2)
print(var3)
print(var4)

#we could also usem* to unpack remaining of tuple
elements=("word","python",12,13)
var1,var2,* var3 =elements
print(var3)
print(type(var3))

#Question

values=("laptop","cable","table","TV","light")

var1,*var2,var3=values

print(var2) #["cable","table","Tv"]
print(type(var2)) #<class 'list'
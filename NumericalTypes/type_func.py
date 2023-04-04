num=21
print(type(num)) #class<int>
 #after the divsion operator
new_var=num / 3 #7

print(type(new_var)) #class 'float'

#Since the result of division (/) operator is not guarented to be
#whole number ,python will always assign result of/operator
#with float number
#------------------------------------------------------------------
# / float sayi verier // tam kesin sayi verir
result_floor =num//3
print(type(result_floor)) # int type

result_intFloat=3.0+5
print(type(result_intFloat)) #class float
#any operator between float and integer will result in 
#float type

#-----------------------------------------------------------------

c=3+0j
print(type(c)) #complex class

#----------------------------------------------

ex="A text"
print(type(ex)) #class str


#ASSIGN MULTIPLE VALUE IN ON LINEnna
x,y,z= "orange","banana","cherry"
print(x)
print(y)
print(z)

















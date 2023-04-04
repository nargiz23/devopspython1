
#Functions we can use
#list()function->will convert other types in list type

t=(1,4)
print(type(t))

new_object=list(t)
print(new_object,"the type of new ibject is",type(new_object))


#============================================================
#len(function)
#len fuction will give us count of total elements in a list
list=[1,2,3]
print(len(list)) #3

#max function=======================================
#helps us find max value
print(max(list))

#min func=======================
#helps us find min value

#=============================
#we can concatenate the lists
numbers=[1,2,3]
words=["Programming","Scripting","Devops"]

new_obj=numbers + words

print(type(new_obj))
print(new_obj) #[1,2,3,"Programming","Scripting","Devops"]









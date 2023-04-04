
#Tuple are immutable storages for python.WE could memorize them as imutable brother of 
#lists
#
#To create a tuple we could use one of three ways below:

#Generic 1 way
nums=(1,2)

#without parenthesis..we could just separate values with comma
nums=1,2

#WE could use tuple() function to creat tuples
#list of objects
list_of_elements=["str",[],{}]

#i want to create a tuple out of list,regardless of what is stored in a list
tuple_of_elements=tuple(list_of_elements)
print(type(tuple_of_elements))

#Accesing elements=============================================

#in order to access elements we can use index numbers

words=("words1","words2")
#print(words[3]) error

#Easies way to loop in a tuple would be using loop

tuple_values=(1,2,3,4,6,5,7)
for el in tuple_values:
    print(el)
















    


















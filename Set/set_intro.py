

# create a set object ==================================

set_obj = {1,1,1,2,3}

#How could I learn total number of elements in the set. 
# We could use len function.

print( len(set_obj) ) # 3

# We could add new elements to set using add method.

set_obj.add("New Element")
print(set_obj)

#set object is mutable.-------------

# remove method will remove given value from set object but if given value
# doesn't exist in a set object, it will generate an error. 

set_obj.remove("New Element")
print(set_obj)


# set discard method  will remove given value from set object but if given value
# doesn't exist in a set object, it will do NOTHING. 

set_obj.discard(3)
print(set_obj)





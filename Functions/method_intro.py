# Creating methods and using

#Methods in python we'll be used for creating algorithm or 
# creating solutions to existing problems. 
# Methods will not get executed(run) unless they are called. 
# When creating a method def keyword needs to be used. 

def greeting():
    print("Welcome to our code")

#Formulate the syntax of methods:
# def name_of_method():
#   #code for method.

# To be able to call the methods we could just use their name.
greeting()

print(greeting())

# None means there is no value
# When there is no value returned from the method, 
# that method returns None.


def second_method():
    return "this value comes from second method"

print(type(second_method())) # -> str

print(second_method())

str = second_method()
print(str)


#Note: print function will display values put in a print function.

#Note; When return keyword is used in a method, 
# we could return a value from that method. 
# And that value can be used later in the code. 
# On the other hand we could not use outputs of the print function
# later in the code. 

















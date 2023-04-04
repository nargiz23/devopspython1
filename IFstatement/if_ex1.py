
#ask user what fahrenheit is weather ?
#if weather is below 32F
#print "It is freezing outside!!!",otherwise 
#printt "it is not bad weather for Chicago"

weather_f=int(input("what is the  weather in Fahrenheit:"))
if weather_f < 32:
    print("It is freezing outside!!!")
if weather_f>32:
    print("it is not bad weather for Chicago")

#is there a possibility that weather is bigger than and also smaller 
# than 32

#since only one of the if statement above can be true,
#it is Best practice to combine these two if statement
 
 # Elif-------------------------------------------------------------------------
weather_f=int(input("what is the  weather in Fahrenheit:"))

if weather_f>32:
    print("it is not bad weather for Chicago")
elif weather_f < 32:
    print("It is freezing outside!!!")

# Elif will get executed ONLY when the previous conditions are false.
# if condition before the elif is True the python interpreter,
# will not check the elif statement. Which result in smoother,
# and more efficient programming. 
#--------------------------------------------------------------
#Else:

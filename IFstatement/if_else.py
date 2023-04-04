
#if the given grade for student is A print
#"that's an excellent grade"
# if the given grade for student is B print
#"that's a good grade"
#in all other grades just print 
#your grade should be improved

#only one of the above condition can be true

grade=input("please enter your grade letter--->").upper()
#what are we expecting from us?
#we used.upper method after the input because in our if statement
#we are expecting grade text to be given in an uppercase letter
#any input will be converted to upper case so that our code can work in both stataement




if grade=="A":
    print("that's an excellent grade")
elif grade=="B":
    print("that's a good grade")
else:
    #when the grade is not A or B
    print("your grade should be improved")

#Python way of saying in all other conditions is using else statement
#else statement gets executed will all previous conditions are False

#what happens user enters a lowers case grade?













number_of_students=34

description= "Total number of student is {}"
print(description)
#Curly braces didnt have any func in this case.Just printed
#as it is in the string

######Format method

print(description.format(number_of_students))

number_of_teachers=3

ratio_description="Total number of students is {} and number of teachers is {}"
print(ratio_description.format(number_of_students,number_of_teachers))
#Total number of students is 34 and number of teachers is 3 
#------------------------------------------------------------------------------------
#NOTE: The braces in the formatted string can be indexed and they will get the parameters
# in order of their index numbers

ratio_description ="Total number of students is {1} and number of teachers is {0}"
print(ratio_description.format(number_of_teachers,number_of_students))
#Total number of students is 34 and number of teachers is 3

#-----------------------------
#we can format the string using f-string

student_name="John"
print(f"The name of the student is {student_name}")

number_of_fruits=10
str=f'The number of fruits we have is {number_of_fruits}'
print(str)


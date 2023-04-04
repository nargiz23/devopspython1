
# Ask user to give you two integer numbers. 
# Find the sum of these two integer numbers. 
# If sum of these two integer is smaller than 10 
# print sum of these two numbers is 10 
# if sum of these two number is between 10 - 19 inclusive, 
# print sum of these two numbers is 20
# For all other conditions 
# print the actual sum of these two numbers.

number1=int(input("enter first number:"))
number2=int(input("enter an other number:"))
sum=number1 + number2
if sum< 10:
    print ("sum of these two numbers is 10 ")
elif 10 <=sum <=19 :
    print("sum of these two numbers is 20")
else:
    print(f"Sum of these two numbers {sum}")


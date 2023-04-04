
#ask user to enter two numbers that are not samme
#and print all numbers that is divible ny 3 and 8
#given 2 numbers
# 


num1=int(input("enter a positive int number:"))
num2=int(input("enter a number bigger than first number:"))

#i have to check range of given numbers
#staring from num1 and num2

while num1 < num2:
 #How can i understand if number is divible by 3 and 8
 #when the remainder gives 0 ,it means we can divide that number
    if num1 %3==0 and num1 % 8==0:
        print(f"{num1} is divible by 3 and 8")


    #for condition update i chould increase the value of num1 
    num1 += 1
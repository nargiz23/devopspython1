
#The three digit number created below 
#num=347
#create a python code to find product of digits from that number.
#the code created should work
#even the value of the variable num changes

num = 513

# Extract the digits from the number
#digit1 = num // 100
#digit2 = (num // 10) % 10
#digit3 = num % 10 last digit gives

# Calculate the product of the digits
#product = digit1 * digit2 * digit3

# Print the result
#print("The product of the digits in", num, "is", product)

#when we find remainder with 10 we always get last digit 
#2%  10-----give us answer 2
#15  %10----5
# 103  %10---3
# 143  % 10--3
#97 %10 --7

#To be able  to find  alst digit of variable num
#

#when  use floor dividion  with number 10 last digit diseaper
 #17 //10=1
 #100//10=10
 #150// 10=15
 #237// 23

###REMAINDER WITH 10 GIVES YOU LAST DIGIT OF NUMBER
###FLOOR DIVISION BY 10 REMOVES LAST DIGIT



last_digit=num % 10 # num=513 // 10 bolunce sonuc 3
first_two_digits= num//10 
#51 = 
middle_digit=first_two_digits % 10
#1
first_digit=first_two_digits // 10 # 51 floor div //10 = 5
#3
print(first_digit * middle_digit *last_digit)
       #5       * 1 * 3








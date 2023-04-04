#we need to write a program to give most efficient
#coin exchange for given dollar amount
#such as if we need to convert'
#1 dollar in to a coin exchange you would 4 quarters
#coun values
#quarter is 25
#dime 10
#nickel 5
#penny 1 cent

given_amount=3.67


#steps to solve
#Pseudo Code
#1.first creat var
#2.to use a single  unit i will convert 

total_cents= given_amount*100 
#total_cents=int(given_amount*100 ) using casting types

#i have to find quarters
q=25
amount_of_quarter=total_cents//q
remainder_after_q=total_cents %q

d=10
amount_of_dimes=remainder_after_q //d
remainder_after_dime=remainder_after_q % d

n=5
amount_of_nickles=remainder_after_dime //n
amount_of_pennies=remainder_after_dime % n

print("Amount of quarter is",amount_of_quarter)
print("Amount of dimes is",amount_of_dimes)
print("Amount of nickels is",amount_of_nickles)
print("Amount of pennies is",amount_of_pennies)




#USE CASTING ONE TIME OUTPUT DECIMAL POINT
#to find that get  float types from the assignment
#you can get float types as a result 

#use casting types














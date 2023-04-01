
b1 =True
b2 =False

print(b1 and b2)
#when used and operator suppost to be both side true

print(b1 and True) #true

print(b2 and b2)

#i want to see if i can go eat todayv
#i have given parameters which are money ,if i have time

have_time=False
have_money=False
can_i_go=have_time and have_money
print("Value of variable can_i_go is",can_i_go)

#OR_________-------------------------------------------------

#i need to exercise everyday.To be able to exercise
#everyday i have to 2 parameter which are if i have my gym card
#or gym equirment at home.in both times i can exercise daily

have_gym_eq=True
have_gym_card=False
can_i_exercise = have_gym_eq or have_gym_card
print("Value of variable can_i_exercise",can_i_exercise) 
#True

#NOT operator------------------------------------------true
#makes boolean value take the opposite value in equation

b2=True
print(b2 and not False)
#output True

print(not b2 and True)
print("The value of b2 is",b2)
#What shouyld be the output? 
# 1: False
# 2: The value b2 is True
#Note: b2 didn't change its value because boolean is an immutable
# type, which means value will be protected unless reassigned.





print(15.6//2)




























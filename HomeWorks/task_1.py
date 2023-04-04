
quarters = int(input("enter how many quarters:"))
dimes = int(input("enter how many dimes:"))
nickels = int(input("enter how many nickles:"))
pennies = int(input("enter how many pennies:"))

# calculate the total value in cents
total_cents = (quarters * 25) + (dimes * 10) +( nickels * 5) + pennies
               #3*23=75           2*10=20       1*5=5          4

dollars = total_cents / 100
cents = total_cents % 100

# print the result
print("\"$",dollars,"\"")
















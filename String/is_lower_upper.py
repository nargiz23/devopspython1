
s="Python"

print(s.islower())
#this will print False because string has upper case letter

s="python"
print(s.islower()) #True

s="python is fun"
print(s.islower()) # TRue

s.upper()
print(s.isupper())# False

s=s.upper()
print(s.upper()) #True
#Unless reassighned value of string NEVER changes

#islower returns TRue when all letters in string is a lower case
#isupper returns True when all letters in string is upper case
#NOte!!! when there is no letter in  sting ,both method will return #False

print("123445".islower()) #false
print("12345a".islower) #True
print("12345A".isupper()) #False








# Ask user to give two different string values
# If the first string contains the second string 
# print True, if not print False.

str1 = input("Enter the first string value: ")
str2 = input("Enter a different string value: ")

# how can I find if str1 contains str2 ? 

# We found number of second string in the first string. 
condition = str1.count(str2) > 0

print(condition)


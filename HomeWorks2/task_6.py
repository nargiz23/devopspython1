
# Write the program to get the string value from the specified position.
# First, ask the user to enter one String value. Then ask the user to the
# enter starting number and ending number. After that, print the value
# between the given starting and ending numbers. (Note: since the user
# does not know the python, the user starts counting from 1, and the
# ending number will be included)
# Example:
# Please enter the String value:
# Definition of Science
# Please enter the starting number:
# 2
# Please enter the ending number
# 5
# The output is:
# efin


string = input("Please enter the String value: ")
start = int(input("Please enter the starting number: "))
end = int(input("Please enter the ending number: "))

start -= 1
end -= 1
substring = string[start:end+1]

# Print the result
print("The output is:")
print(substring)


# Ask user to enter any string value using input function.
# Then, remove ALL THE SPACES (" ") from the given string.
# After removing the spaces from the string,
# if the string's length is odd print True, otherwise print False.
# Example:
# Input : I love coding
# Output: True
# Input : one two
# Output: False 

string = input("Enter a string: ").replace(" ","")
print(len(string))
if len(string) % 2 == 1:
    print(True)
else:
    print(False)




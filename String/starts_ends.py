
s1="AI is future"
s2="future!!"

print(s1.endswith("future")) #False

print(s1.endswith(s2))## True

print(type(s1.endswith(s2))) #class bool

#startwith method will  only return true if the str start with
#given parameter

s1="AI is future!!"

print(s1.startswith("another string")) # False

print(s1.startswith("A")) # True

print(s1.startswith("AI is fut"))  # TRue

print(s1.startswith("ai")) # false
print(s1.endswith("FUTURE")) #fALSE

#bOTH  STARTS AND ENDSWITH METHODS ARE case sensetive


# Ask user to give two string values and 
# print True if the second string starts with 
# last two charachters 
# of the first string OR print True 
# if the first string starts with
# first two charachters of the second string.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

start_last_two= string2.startswith(string1[-2:])
print(" The second string starts with the last two characters of the first string.",start_last_two)
start_first_two=string1.startswith(string2[:2])
print("The first string starts with the first two characters of the second string.",start_first_two)






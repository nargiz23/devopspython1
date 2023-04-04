
#ask user to enter a word
#print True if the first and last letter of the sting is same
#otherwise print False

str=input("please enter a word:")
first_letter=str[0]
last_index=len(str)-1
last_letter=str[last_index]
print(first_letter == last_letter)


print(type(first_letter)) #class 'str'
print(type(last_letter)) #class 'str'




# Ask user to give a string filled with cat and dog words
# From the given string if the number of dogs 
# and cats  is the same print True,
#  other wise print False

# catdog -> True
# catcatdog -> False

given_text=input("give a string filled with cat and words:")

number_of_cat=given_text.count("cat") #0
number_of_dog=given_text.count("dog")
print(number_of_dog==number_of_cat)


# if the it finds the provided character of the string it will return 
# total number of those character. If those characters does not exist
# in string it will return 0.\

print("".count("academy"))
print("Academy".count("Academy"))






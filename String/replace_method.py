# Given a string, return a version where all 
# the “x” have been removed.
# Except an “x” at the very start or
#  end should not be removed.
# “xxHxix” → “xHix”
# “abxxxcd” → “abcd”
# “xabxxxcdx” → “xabcdx”

str=input("enter a string:")
#I should replace all the "x" with empty string value
replace=str.replace("x","")
print(replace)

#I will save first and last letter from string
first_letter=str[0]
last_letter=str[len(str)-1]

# i should get a part of string where first and last letter is not included
mid_str=str[1:len(str)-1]
print(mid_str)

end_result=first_letter + mid_str.replace("x","") + last_letter
print(end_result)


#Ask user to enter a string and a rotated
#left2 version where the first 2 characters
#of the string moved to the end
#"Hello "---"lloHe"
#"mute"---temu
#"techtorial---chtorialte"

#input func allow us to get values when we ran the code rather than
#giving in the begining of coding
#usinn input finction we can get str variable,which will help
#us to work with dynamic values

str=input("Enter a strng value:")
#first 2 character from given str
first_two=str[0:2]
rest_of_str=str[2:]
 
end_result=rest_of_str + first_two
print("Rotated left 2 version of variable str is",end_result)





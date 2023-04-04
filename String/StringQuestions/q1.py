
#ask user to enter a str
#print a version of that string without first and last letter
#you can assume that user will give a str lenght more than 2
#table----abl
#keyboard ---- eyboart

string=input("enter a string:")
# i need to return this str without first and last letter
#1.way
print(string[1:len(string)-1])

#2.way
 #since the python has negative indexing the code
 #without first and last chractre

print(string[1:-1])
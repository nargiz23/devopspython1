#Slicing with the steps
s="TechTorial"

substr=s[3:8:2]

print(substr)

sub=s[2:4:-1]
print(sub)
print(len(sub))
#since slicing will go from right to left because of the negative step
#the code wll not be able to find index 4 after starting forom
#index number2.therefore the variable sub wilbe an empty string
substr2=s[4:2:-1]
print(substr2) #output TH


#Question1
print(s[:] == s)

#q2
print( s[:]==s[::1] ==s==s[0:len(s):1]==s[0:len(s)])
print(s[::-1]) #reverse of s==Techtorial





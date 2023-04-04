#indexes 012345678
text=   "Python is a programming language!"

part1=text[2:6]# thon
print("When we slice from index 2 to 6 the sliced part is",part1)
print("The lenght of sliced part is",len(part1))

part2=text[6:3]
print("When we slice from index 6 to 3 the sliced part is",part2)
#slicing goint only left to right
#right to left error
print("the bool value of the sliced str will be",part2)


#------------------------------------------------------------------
#Omitting starting or ending index
#we will cober the ouptut when ending or starting index
#is not provided

substr=text[:4]
print("When we slice from index 4 is",substr)
print("The length of sliced part is ",len(substr))
#When starting index is not provided,sliding will start from
#index0
#text[0:4] is exactly same as text[:4]

substr2=text[1:]
print("When we slice without ending index starting 1",substr2)
print("The length of sliced part is ",len(substr2))
#when the ending index for a slicing is not provided it will go 
#till the end to string



#Reverse a given str  usinging for loop with range fuction
#dont use slicing strings
#0 to last index
#o to len-1 last index

#when negative step is used for range func ,start and
#stop points shoul reverse.we still hsve to keep in mind that
#starting index is included and ending index is not
#

str=input("enter a str:")
for index in range(len(str)-1,-1,-1):
    print(str[index],end=" ")
print()

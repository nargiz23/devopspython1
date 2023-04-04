
#set uniuon method--->will combine elements of both set

s1={1,3}

S2={"str1","str2"}
new_set=s1.union(S2)

print(new_set) #{1,3,'str2,'str1}

print(s1) #its not changed after union method

print(S2)  #its not changed after union method

#Set intersectionmethod-----will return only common elements from both
#sets

new_set=s1.intersection(S2) 
print(new_set)



#NOTE:Empty set in python is not shown will empty braaces,
#empty set is represents by set functions
#the reason for that empty braces in python represents a dictionary
#object



#Differents method=====================================

#will return a different elements from both sets as  a new set



s1={1,3}

S2={"str1","str2"}

#The method bellow will return elements that is in the
#s1 both not in s2
new_set=s1.difference(S2)

print(new_set)




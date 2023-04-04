
a=(2,3,5,7,10,11,0,1)
#sort this tuple and print result

#can we change the order of items in a tuple?
#no we cannot because tuples are immutable
#if i can convert this tuple in to a list object,
#then i could sort it

a=list(a)
a.sort()
a=tuple(a)

print("Type of a is",type(a),f"and value of a is {a}")
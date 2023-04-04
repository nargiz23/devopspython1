
numbers = [2, 5, 8, 3, 6, 4, 1, 7, 0, 9, 2, 5, 6, 1, 8]
numbers.sort()
# We should find all pairs of numbers that add up to 9. 
# At the end of the task, we should only print unique pairs. 
# Also, make sure in the pairs bigger element shown first.

# Print all the values from this list using indexes.
set_obj = set()
for index in range(len(numbers)):
   # print(numbers[index])
    for index2 in range(index+1,len(numbers)):
        if numbers[index] + numbers[index2] == 9:
            #2 + 5==7==9
            my_pair = ( numbers[index2],numbers[index] )
            set_obj.add(my_pair)
print(set_obj)            
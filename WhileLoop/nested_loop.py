
#Lets's print
#ASk user to how many lines of output they would like to see
#our lines should like
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#I could print the numbers from 1 to 5 inclusive
limiting_line=int(input("Enter a number of line you would like to see:"))
line_number =1
#for each line i  have to print numbers from 1 to the line number inclusive
while line_number <= limiting_line:
   # print(f"you can see the line number{line_number} on the below")
    #for each line i  have to print numbers from 1 to the line number inclusive
    numbers=1
    while numbers <=line_number:
        print(numbers,end =" ")
        numbers +=1
    print()
    line_number +=1



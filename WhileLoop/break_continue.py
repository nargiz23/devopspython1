
#When the code execute break statement the loop will stop ,even
#the conditio for a loop is true

while True:
    print("Example of a break statement")
    break #meaning don't check again  loop is done
#The loop above will iterate 1 time.


#Continue-------------------------------------
#in order to star next iteration in the loop rather than waiting for
#all loop of a body to execute we can use continue statement

#lets print all number from 1 to 20 inclisive,
# if they are an odd numbers print the numbers
 #NOTe Odd numbers is:1,3,5,7,9.....

count=1
while count <= 20:
    if count % 2==0: #Which means the count is an even numbers
        count +=1
        continue
    print(f"{count} is an odd number.")
    count +=1

#NOTE :continue statement is not used commony when codding
#continue dosun't change output,however it makes
#code little faster

#pass is used for having an empty indented body, continue is used for jumping to the next
# iteration.

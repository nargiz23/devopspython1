
#range func with one parametre
print(range(5))

print(type(range(10)))  # class'range'

#Just check the first 5 index number of string
#print true etc...

str="table"
for index in range(5):
    print(str[index])


#ex-----------------------------------
#print all eveb numbers from 1 to 10 inclusive(dahil)
for number in range(1,10):
    if number %2==0:
        print(number)



#NOTE/:indentation after while,for, if statements
#required,however indendation doesn't have to be 4 space.or tab
#in order to make code more readible and undersantable
#use 4 space all time

#RAnge fuction with three parameters
#range(start,end,step)

#Print all the even numbers from 1 to 10 inclusive

for num in range (2,11,2):
    print(num)






#create a func that takes any count of number or numbers
#find sum of all given numbers
#the function can get 4 number parameter  or 12
#in order to be flexeble (istedigin numarayi almasi icin tupe daki * kullaniliyor
#we could take will use * symbol before the name)

def find_sum(*numbers):
    print(type(numbers))
    pass
#i shoul treat this numbers variable as a tuple
    sum=0
    for num in numbers:
        sum +=num
    return sum
print(find_sum(30,20))




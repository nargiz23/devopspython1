
#Calculate if the given year number is the leap year or not. 
# if it is a leap year we'll print True, if not we'll print False. 

#A leap year is a year that is evenly divisible by 4, 
# unless it is a century year (divisible by 100), 
# in which case it must also be divisible by 400 to be a leap year.


#Solution
#if the year is divisible by 4 it is a leap year
#it's should't be a centure year(1800)
#when it is  a century year and also divible by 400 then
#it is a leap year

#it should check if the year divisible by 4 but not 100
#i should check if year is divible by 400


year=2400
is_leap=(year%4==0 and year % 100 !=0) or( year % 400==0 )
         #True   and      #False=  False         #true
print("The condition of the given year being a leap year is ", is_leap)
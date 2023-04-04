
#Create a function to find highest common factor of two given numbers
#HIghest common factor is biggest common divisor of two given numbers.
#24 18 6

#What is the limit of the numbers i should check as possible HCF
#i have two given numbers,my limit as possible HCF should be one of the numbers and below
#i should choose one of the numbers start checking from that number to number1.
#when writing a code first do neccessities of the code than optimized
#Lowes iteration possible.What is the biggest possible common divisor
#bigger number divided by 2 is the biggest possible divisor unless they are the same

def find_hcf(num1, num2):
   possible_hcf=num1
    #possible_hcf=max((num1,num2)) //2
   while True:
      if num1 % possible_hcf ==  0 and num2% possible_hcf == 0:
         #it is not a possibilty that possible hcf can divide both
         #it is a certainty
         return possible_hcf
      #I should tell code look next possible optoin
      possible_hcf-=1 #11 10 9 

print(find_hcf(24,32))
print(find_hcf(32,24))

print(find_hcf(32,12))

#ask user to enter a string.
#print all the vowels and count of vowels from the given string
#vowels in alph are a,e,i,u,o



string=input("Enter a string:")
count_of_vowels=0
index_in_str=0
vowels_in_given_str=''

while index_in_str < len(string):
    vowels="aeiou"
    current_letter= string[index_in_str]
    #if the current letter is one the chars from vowels string
    #it means we have to increase count of vowels.
    #in order to check if current exist in vowels str
    if current_letter in vowels:
      count_of_vowels+=1
      vowels_in_given_str=vowels_in_given_str +current_letter

    index_in_str +=1
print(f"The all vowels in string order is  {vowels_in_given_str}")
print(f"Amount of vowels we have in the given string is {count_of_vowels}")


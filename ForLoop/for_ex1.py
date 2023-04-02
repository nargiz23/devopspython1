
#print given string withouts its vowels using for loop and continue statement

str=input("erter any string:")

# i should check each letter indivially so that i can evalute
#whether they are consonant or vowel
vowels="aeiouAEIU"
for anything in str:
    if anything in vowels:
        #it says that el is a vowel.
        continue
    print(anything,end=" ")

print() # to get of percent sigh that appears others
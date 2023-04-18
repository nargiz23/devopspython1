

bjnmm=1
ccgb=3
sum=bjnmm +ccgb
print (sum)
def ispalindrome(word):
    #i need to reversed version of given string
    reversed=word [::-1]
    return reversed.lower()==word.lower()

word=input("enter a word:")
print(ispalindrome(word))

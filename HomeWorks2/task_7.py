# 1. Ask the user to enter a random word using input function.
# 2. Then ask the user to input the number of letters that word consists of.
# 3. Lastly ask the user for a letter that they want to learn its index.
# 4. Your code should print True if the user entered a right number of letters in the
# word. Print False if the wrong number is entered.
# 5. Your code should print the index of the entered letter, if the word doesn’t
# contain the letter then the code should print -1.
# 6. Please look at the example output below to understand how your code
# should work.
# EXAMPLE OUTPUT:
# Enter a random word
# Techtorial -> this line represents user's input
# Enter number of letter that word consists
# 10 -> this line represents user's input
# True
# Enter a letter that you want to find an index
# a -> this line represents user's input
# 8


word = input("Enter a random word: ")
length = int(input("Enter number of letters that word consists of: "))
if len(word) == length:
    print("True")
else:
    print("False")
letter = input("Enter a letter that you want to find an index: ")
if letter in word:
    index = word.index(letter)
    print(index)
else:
    print("-1")

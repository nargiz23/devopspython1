
# Using the input function ask the user to enter one sentence with three
# words and print the index number of each word's last character and then
# print the sum of each index number that you found.
# For Example:
# Input:
# "Importance of Human" --> it can be any three-word sentence.
# Output:
# 9 --> index number of 'e'
# 12 --> index number of 'f'
# 18 --> index number of 'n'
# The sum: 39


sentence =input("Enter a one sentence with three words: ")

first_word_index = sentence.find(" ")-1 # first word
print(f"Last character of first word index {first_word_index}")
second_word_index = sentence.rfind(" ")-1   #second word
print(f"Last character of second word index {second_word_index}")
last_word_index = len(sentence)-1   # third
print(f"Last character of last word index {last_word_index}")
result = first_word_index + second_word_index + last_word_index  # sum
print("The sum:",result)


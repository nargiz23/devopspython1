



#we need to find count of each word from given str
 #we know that each word in str separated by speace
 #if there was a way that i could separate all string from spaces and store 
 #

 #Split=============================================================
#text="we are coding"
#print(text.split(" "))




text = input()

# We need to find count of each word from given string. 

# We know that each word in string separated by space. 
# If there was a way that I could separate all string from spaces and store it somewhere
# I could at least find each word from string. 

#using split method I could get each word indidually. 
# split method divides string and puts in a list. 

words = text.split(" ")
print(words)

words_and_counts ={}
for word in words:
    if words_and_counts.get(word) == None:
        words_and_counts[word] = 1
    else:
        existing_count = words_and_counts.get(word)
        updated_count= existing_count + 1
        words_and_counts[word] = updated_count

print(words_and_counts)























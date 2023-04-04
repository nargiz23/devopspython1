
#ask user to enter a string that has 2 word doesn't start with empty space
#if user enters a space in the beginning or
#a string that has more than or less than 2 words re ask use \
#to enter a string

shoul_i_ask=True
while shoul_i_ask:
    print("enter a string that has 2 word doesn't start with empty space:")
    input_str=input()
    #string doesn't start with
    if not input_str.startswith('') and (input_str.strip().count(" ")==1):
        print(f"You have entered a correct string by entering{input_str}")
        shoul_i_ask=False

#NOTE!! strip method removes all spaaced at the end or beginning of string.
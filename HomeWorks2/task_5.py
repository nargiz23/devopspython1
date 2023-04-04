
# Using an input function enter three different ingredients for the product
# on the same line. Then ask the user to enter any int number.
# Change the first letter of the ingredients starting from the entered number.
# (Ingredients should start with different letters. Please read the example
# carefully )
# Example 1:
# Please enter three ingredients with spaces:
# Milk Peanuts Butter
# Please enter the int number:
# 5
# The output is:
# 5ilk 6eanuts 7utter


 #Example1
ingredients = input('please enter 3 different ingredients ->') #Milk Peanuts Butter
user_int = int(input('Please enter a number ->') )
updated_str= ingredients.replace(ingredients[0:1],
str(user_int)).replace(ingredients[ingredients.find(' ')+1],
str(user_int+1)).replace(ingredients[ingredients.rfind(' ')+1],
str(user_int+2))
print(f"The output is:{updated_str}")

# Example 2:
# Please enter three ingredients with spaces:
# Sugar Cocoa Oil
# Please enter the int number:
# 3
# The output is:
# 3ugar 4ocoa 5il

#Example 2
ingredients = input('please enter 3 different ingredients ->') #Sugar CoCoa Oil
number = int(input('Please enter a number ->') )
new_str= ingredients.replace(ingredients[0:1],
str(number)).replace(ingredients[ingredients.find(' ')+1],
str(number+1)).replace(ingredients[ingredients.rfind(' ')+1],
str(number+2))
print(f"The output is:{new_str}")




# The doctors say  babies can go out in summer if the weather is 
# between 60 and 80 inclusive. If not they say you shouldn't take the baby out. 
# In the winter they say you can go out if the weather is hotter than -20
#Ask user what season they are in also ask user how hot the weather 
# is  and print if they can go out with baby or not.

season=input("enter the current season:")
weather=int(input("enter the current weather F:"))

if season=="summer" and 60 <=weather <=80:
    print("you can go out with baby")
elif season=="winter" and weather>-20:
    print("You can go out with baby")
else:
    print("you shouldn't go out with baby in this waether")
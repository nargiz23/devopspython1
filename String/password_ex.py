
#ask user to enter a password
# the password should contain
#both upper and lower case letters
#if it contains both upper and lower case letter
#print True ,otherwise print False


#we are expecting user to enter a both with lower and uppper case
password=input("enter a password contains upper and lower case:")

#I should write a code if conditions provided or not

#s='password'
#s==s.lower()---> password=='password'.lower()---True
is_all_lower=password==password.lower()

#s= "PASSWORD"
#s==s.upper()---> "PASSWORD"-->'PASSWORD.upper()

is_all_upper=password==password.upper()


is_password_good =not is_all_lower and not is_all_upper
print("The given password is",is_password_good)





#parameters are the datas that are given for afinction(method)
#in that finction usually implementations are done according to
#parameters

#create a method that takes one parameter as full name
#and returns upper case version of that parameter

def upper_case_name(full_name):
    return full_name.upper()

name="John Jessie"
print(upper_case_name(name))

print(name)


# def upper_case_name(full_name):
#     return full_name.upper()

# full_name="John Jessie"
# print(upper_case_name(full_name))

# print(full_name)


new_variable=upper_case_name(name)
print(new_variable)
print(name)

#Number of parameters given to funtion should exactly match
#therefore,code below generate sn error
#upper_case_name()



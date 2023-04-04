
# Please use method chaining for the following Strings. Methods are
# provided next to the String.
# String “ Snicker " —> strip, upper, remove prefix and slice the string with
# any number of your choice
# String “Cookie” —> lower, replace ‘o’ with ‘u’
# , remove suffix e,
# starts with ‘C’

str1=" Snicker "
print(str1.strip().upper().removeprefix("Sni")[2:6])

str2 = "Cookie"
print(str2.lower().replace("o", "u").removesuffix("e").startswith("C"))

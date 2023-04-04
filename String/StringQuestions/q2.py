
#the link of the pages consist of 3 parts
#first part before the the dot its called subdomain
#last part after the second dot is called top.level domain name (TLD)
# mid part(in between the dots) is called domain name

#ask user to enter webside name
#assume that subdomain name will be www and tld will be com
#print the domain name of the user's website link.



link=input("PLEASE ENTER THE LINK OF YOUR PAGE:")
domain_name=link.removeprefix("www.").removesuffix(".com")
print(f"The domain name of your page is {domain_name}")


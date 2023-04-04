

#To able to create a dictionary oj=bject we could use 
#dict() func or we could use curly braces.

d1=dict()
d2={}
print(type(d1)) #'class 'dict'
print(type(d2)) #class 'dict'

#creat one dictionary
# Note: Key and value in dictionary objects are separated by column,
#and key-value Pairs are separated by comma.

laptop={ 
    "brand": "Apple",
    "model" : "Macbook Pro",
    "year"  : "2021"
}

print(len(laptop))

#How do you we could access the elements/?
#dictionary objects don't use indexing
#using Keys in the dictionary object i could retrive associated valuesan

print(laptop["brand"])

#Get() method========================================
print(laptop.get('brand'))
#diffence using get method or [] is when keys not present in square brackets
#will generate an error.In  the get method we wouldn't encounter this error
# 
#print(laptop.get("storage"))-----------> value nONe
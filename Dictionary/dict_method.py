

#value method======================================

laptop={ 
    "brand": "Apple",
    "model" : "Macbook Pro",
    "year"  : "2021"
}
print(laptop.values())
print(type(laptop.values())) #dict values
#Note dict value 

list_of_values=list(laptop.values())
print(f"the value odf list is{list_of_values} and the type is",type(list_of_values))

#Key method=============================================
print(laptop.keys())
print(type(laptop.keys())) #---dict keys

#Note :dict keys objects can easy be converted to set or list object
set_of_keys=set(laptop.keys())
print(set_of_keys)
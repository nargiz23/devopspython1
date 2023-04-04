
student={
  "course":"Devops",
  "name" :"John",
  "start_date":"April",
  "end_date": 'May'

}

for k in student.keys():
    val=student.get(k)
    print("type of key is, ",type(k),f"and the key is {k} and value for the key is{val}")


#"The usage of for loop above is not optimized"
#item method

print(type(student.items()))
print(student.items())
 

 #k=key v=value
for k,v in student.item():
    print(f"The key is {k},the value is {v}")








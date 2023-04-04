
#Since the dictionary objects are mutable,we could change 

student={
  "course":"cyber security",
  "city" : "Chicago",
  "age"  :    29

}

#this partucular student changed interest and to join in DevOps course

student["course"]="DEv Ops"
print(student.get("course"))


#The line below will add a new key- value pair in to dict object.
student['key1']="Dev Ops"
print(student)


#REMOVE================================================

#del keyboards
del student["key1"]
print(student)













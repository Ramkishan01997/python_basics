# dictionary in python 

info={
    "name":"ram",
    "age":27,
    "lname":"suryawanshi",
    "marks":["test","kishan","suryawanshi",34],
    "percentage":86.45
}

print(info)
print(type(info))
print(info["name"])
# info.values("test":"bkjhkj")
info["name"]="ram kishan"
print(info)
print(" all values",info.values())
#  create new dictionary to store student details
students={
    "name":"user1",
    "marks":{
        "chem":34,"math":89,"english":77
    }
}
print(students["marks"])
print(" print chemistry marks :",students["marks"]["chem"])

print(students.get("name"))
## updating values
city={"city":"pune"}
students.update(city)
print(students)

###Set in python

numbers ={1,3,4,2,3,4,"test","python"}
print("all values in set",numbers)
print(type(numbers))
print(len(numbers))
## initialize empty set
set1=set()
set1.add(1)
set1.add("name")
set1.add("java")
print(set1)
set1.remove(1)
print(set1)
set1.clear()
print(set1)
num=0

set2={1,2,3}
set3={2,4,5}
print(set2.union(set3))
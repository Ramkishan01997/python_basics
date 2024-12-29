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
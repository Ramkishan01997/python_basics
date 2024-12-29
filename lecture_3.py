# list is built in data type that store set of values
marks=[23,34,56,90,12]

print(" marks : ",marks)

students=["ram",34,34,"test"]
print(students[:1])
print(len(marks))
marks.sort(reverse=True)# list.sort()
print(marks)
students.append(4)
print(students)
students.reverse()
print("reversed list :",students)
#####

students.insert(1,"tyyy")

print(" check inserted values: ",students)



### tuple is immutable
name=(1,2,3,2,4)
print(name)
print(name[1])
# name[1]=5
print(name.count(2))

# write a program to insert movies name in list

movies=[]
mov1=input(" enter name of mives :")
mov2=input(" enter name of mives :")

# movies.add(input(" enter movies name"))
movies.append(mov1)
movies.append(mov2)
movies.append(input("enter 3rd movies name :"))
print(movies)

#### program to find list is palindrome 121==121
list1=[1,2,1]
list2=list1.copy()
list2.reverse()
if(list1==list2):
    print("list is palindrome")
else:
    print("list is not palindrome")

# write program to count grade A in tuple
grades=('A','B','E','B,','C','A')
grade=input(" enter the grade ..:")
print(" no of students with A grade ",grades.count(grade))

### list grades1
grades1=['A','B','E','B,','C','A']
grades1.sort()
print("sorted graded :",grades1)
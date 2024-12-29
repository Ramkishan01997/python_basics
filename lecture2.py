s1="name is  ram"
s2="selenium"
s3='java'
s4="""python"""

print(s1+s2)
print(len(s1))
print(s1[2])
# for x in s1 :
#     print(x)

print(s1[4:])

#   
str1=" java is a language"
print(str1.endswith("age"))## True
print(str1.endswith("vbibi"))## False
str2=str1.capitalize()
print(str2)
print(str1.count('is'))

##Loops in python 

light=input(" Enter the value :")

if(light=="red"):
    print(" stop ...")
elif(light=="green"):
    print("Go ...")
else:
    print(" wait ...")
 

age=20

if(age>18):
    if(age<80):
        print("eligible for licence")
    else:
        print("age is greater than expected")
else:
    print("your  are not eligible for driving test")


### even odd program

num=5

rem=num%2

if(rem==0):
    print(num," is even number")
else:
    print(num," Is odd number")

# find gretest number among three number

a=input("enter first number :")
b=input("enter second number :")
c=input(" enter third number :")

if(a>b and a>c):
    print(" a is grater number",a)
elif(b>c):
    print( b," is greatest number")
else:
    print(c,"is greatest number")


    # Define the file name and content
file_name = "example.txt"
content = "vbljbbi jlbljbkjl bjbjlhvb jlhv vj ooijj"

# Create and write to the file
with open(file_name, "w") as file:
    file.write(content)

print(f"File '{file_name}' has been created and the text has been written to it.")

with open(file_name,"r")as file:
   print(f"reading file '{file_name}'",file.read())
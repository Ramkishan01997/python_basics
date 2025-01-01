def factorial(n):
    if n<0:
        print(" factorail of negative not possible")
    elif n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact

number=int(input(" enter the number"))
result=factorial(number)
print(f" factoril of '{number}' is a '{result}'")

# write a program to find sum of n number

x=5
sum=0
for i in range(1,x+1):
    sum+=i
print(sum)

## factorial
c=6
facta=1
i=1
while i <=c:
    facta*=i
    i+=1

print(facta)


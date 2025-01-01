def calculate_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calculate_sum(4,5)
calculate_sum(6,9)

def cal_auv(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg

print(cal_auv(2,3,4))

## defualt parameter
def cal_diff(b=2,a=1):
    diff=b-a
    return diff

print(cal_diff())
print(cal_diff(5,3))
cities=["pune","hyderabad","nanded","Nashik"]

def len_cities(list):
    lenth=len(list)
    return lenth

name=["ram","kishan"]
print(len_cities(cities))
print(len_cities(name))
def printcites(list):
    for i in list:
        print(i,end=" ")

printcites(name)
print()
def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact_num(10))

def convert_to_rupee(num):
    rupee=num*80
    print(num," USD =",rupee," India Rupee")

print(convert_to_rupee(10))

#recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if n==0 or n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

def sum1(xn):
    if(xn==0):
        return
    # print(n)
    return sum1(xn-1)+xn

print(sum1(3))
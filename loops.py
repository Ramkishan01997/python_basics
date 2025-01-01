count=1
while count<=5:
    print("hello")
    count+=1
print("loops ended ")

# while
num=1
while num<=100:
    print("num",num)
    num+=1

num1=100
while num1>=1:
    print("num1",num1)
    num1-=1

list=[1,4,9,16,25,36,49,64]
print(len(list))
n=0
while n<len(list):
    print(list[n])
    n+=1

tnum=(3,4,5,6,7,8)
tx=5
i=0
while i<len(tnum):
    if(tnum[i]==tx):
        #  continue
        print(tx,"found at indec :",i)
        # break
    i+=1
    print("searching ",i)

c=1
while c<=10:
    if(c%2==0):
        c+=1
        continue
    print(c)
    c+=1

###
numlists=[1,3,5,6,7]

for el in numlists:
    print(el)
 
tupl=(3,5,6,'ree',4)

for tpl in tupl:
    print(tpl)

nmname="ramkishan"

for nm in nmname:
    print(nm)

example1=[1,4,9,16,25,36,49,84,81]

for ex in example1:
    print("elememt in list :",ex)

exampletuple=(1,4,6,7,9,10)

for etpl in exampletuple:
    if(etpl==4):
        print(etpl," found at :")
        break
    print("...searching..")

## range()
print(range(5))
for i in range(5):
    print(" numbers is :",i)

for i in range(1,100,5):
    if(i%2==0):
        print(i)
    i+=1

for x in range(4):
    pass
print("test")


n = 5
for i in range(0 , n):
    for x in range(0,i):
        print("*",end = " ")
    print(' ')

for z in range(n,0,-1):
    for a in range(z):
        print('* ', end="")
    print('')

n = 8                     
list = [None] * n         
print(list)
list[1] = "A"
print(list[1])
print(list)
index = list.index(None)
print(index)
for x in range(0,len(name),):
    input("what is your name: \n ")
    name[x]


n= 8
list = [None]*n
for x in range(0,len(list),1):
    list[x]=input("Enter your name: \n")
    
print("your name in reverse format is : \n")

for z in range(len(list),0,-1):
    a = z-1
    print(list[a], end = ' ')


x = 0
y= 0
n = int(input("enter the term inating condition: "))
while x<=n:
    print(x)
    y = x
    x  = y + x
    
    fibonaci series:
x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y


print("\t\t   ****")
n = 5

for i in range(0,n):
    print("\t\t*       *")
    

print("\t\t   ****")

n=5
for i in range (0,n):
    print("*")
print("*****")


a = int(input("enter the first side:  "))
b = int(input("enter the second side:  "))
c = int(input("enter the third side:  "))


if(a == b == c):
    print("Equilaternal Triangele")
elif(a != b != c):
    print("Scalene Triangle")
else:
    print("isosceles Triangle")    

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))

print(b)


for i in range(10):
     print(str(i) * i)

num = int(input("enter you no: "))
num1 = int(input("enter you no: "))

sum = num + num1

if(sum >= 15 and sum<=20):
    print("20")
else:
    print(sum)

num1 = 0
multipler = int(0)
for num1 in  range(1,11):
    multipler = 6* num1 
    print ("6",'x', num1, '=', multipler)    



k = input("enter the character: \n")

if(k == "a" or k =="e" or k == "i" or k == "o" or k == "u"):
    print("vowel")

num = int(input("enter you no: "))
num1 = int(input("enter you no: "))

sum = num + num1

if(sum >= 15 and sum<=20):
    print("20")
else:
    print(sum)

num1 = 0
multipler = int(0)
for num1 in  range(1,11):
    multipler = 6* num1 
    print ("6",'x', num1, '=', multipler)    



k = input("enter the character: \n")

if(k == "a" or k =="e" or k == "i" or k == "o" or k == "u"):
    print("vowel")

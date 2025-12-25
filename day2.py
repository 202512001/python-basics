
'''even no from 1 to 10'''
for i in range(1,11):
    if i%2==0:
        print(i)

'''while loop'''
i=1
while i<=5:
    print(i)
    i=i+1


'''sum of n no'''
num=int(input("enter no:"))
total=0
for i in range(1,num+1):
    print(i)
    total+=i

print("sum::",total)

'''factorial'''
num=int(input("enter no:"))
fact=1
for i in range(1,num+1):
    print(i)
    fact*=i

print("factorial::",fact)


'''multiplicatio table'''
n=int(input("number:"))

for i in range(1,11):
    print(n, "x", i, "=", n*i)


'''function'''
def greet():
    print("Hellooo")

greet()

'''sum'''
def add(a,b):
    print(a+b)

add(2,3)

'''fun with return'''
def square(n):
    return n*n

res=square(5)
print(res)

'''calc using func'''
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

add(5,3)
sub(10,5)
mul(2,4)
div(4,2)

'''largest of 3 no'''
no1=int(input("no 1:"))
no2=int(input("no 2:"))
no3=int(input("no 3:"))

def largest_no(a,b,c):
    if a>=b and a>=c:
       return a

    elif b>=a and b>=c:
      return b

    else:
        return c

largest=largest_no(no1,no2,no3)
print("we found",largest,"as largest")

'''prime no'''
def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    
    return True

num=int(input("enter no:"))

if is_prime(num):
    print(num,"is prime")
else:
    print(num,"is not prime")
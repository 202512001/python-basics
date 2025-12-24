"""print("Hello, i am shruti")
name="shruti"
age=21
cgpa=6.7
is_student=True
print(name)
print(age)
print(is_student)
print(cgpa)

name1=input("enter name:")
print("my name is:",name1)
age1=int(input("enter age:"))
print("age is:::",age1)

num=int(input("enter num"))
if(num%2==0):
    print("even")

 
else:
    print("odd")

num1=int(input("ente no 1:"))
num2=int(input("enter no 2:"))
if num1>num2:
    print("largest is",num1)
else:
    print("largest",num2)

number=int(input("enter number:"))
if number==0:
    print("number is zero")
elif number<0:
    print("number is negative")
else:
    print("number is positive")"""


no1=int(input("no1:"))
no2=int(input("no2:"))
op=input("select +,-,*,/:")
if op=="+":
    print(no1+no2)
elif op=="-":
    print(no1-no2)
elif op=="*":
    print(no1*no2)
elif op=="/":
    if no2!= 0:
        print(no1/no2)
    else:
        print("can not dev")
else:
    print("invalid op")
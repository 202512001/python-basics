marks=[20,30,40,50]
print(marks)
print(marks[0])
print(marks[-1])

for m in marks:
    print(m)

marks.append(10)
print(marks)
marks.remove(30)
print(marks)
marks.sort()
print(marks)

'''find total and avg'''
marks=[10,20,30,40]
total=0

for m in marks:
    total=total+m

avg=total/len(marks)
print(total)
print(avg)

'''max no'''
num=[30,20,40,10]
max_no=num[0]

for n in num:
    if n > max_no:
        max_no=n

print("max no is:",max_no)

'''dictionary'''
student={
    "name":"Shruti",
    "age":21,
    "course":"msc.it"
}
print(student)
print(student["name"])

student["age"]=22
print(student["age"])
student["city"]="ahm"
print(student["city"])

for key, value in student.items():
    print(key, ":", value)

students = []

no=int(input("enter no of students:"))

for i in range(no):
    print(f"\nenter details of students {i+1} ")

    sid=int(input("s id:"))
    name=input("s name:")
    marks=int(input("s marks:"))

    student={
    "id":sid,
    "name":name,
    "marks":marks
    }

    students.append(student)

print("now detailss:")
for s in students:
    print(s)

ss_id=int(input("ent id:"))
found=False

for student in students:
    if student["id"]==ss_id:
        print("that student:")
        print("his name:",student["name"])
        found=True
        break

if not found:
    print("not here")

def upd(list,s_id,n_m):
    for student in list:
        if student["id"]==s_id:
            student["marks"]=n_m
            return True
        
    return False

s_id=int(input("enter id to update marks"))
n_m=int(input("enter new marks"))

if upd(students,s_id,n_m):
    print("marks updated")
else:
    print("not updated")

print("updated list")
for s in students:
    print(s)


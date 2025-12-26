students=[]

def add_student():
    id=int(input("enter id:"))
    name=input("enter name:")
    marks=float(input("enter marks:"))

    student={
        "id":id,
        "name":name,
        "marks":marks
    }

    students.append(student)
    print("studenet added successfullyy")

def view_student():
    if not students:
        print("no student found")
        return
    
    print("student list:")
    for s in students:
        print(f"ID:{s['id']}, NAME:{s['name']}, MARKS{s['marks']}")
    print()


def search_student():

    s_id=int(input("enter id to search:"))

    for s in students:
        if s["id"]==s_id:
                print(s["id"], s["name"], s["marks"])
                return
        
    print("student not found")

def menu():
     while True:
        print("student management system")
        print("1.add student")  
        print("2.view student") 
        print("3.search student") 
        print("4.exit")

        choice=input("enter choice(1-4):")

        if choice=="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice=="3":
            search_student()
        elif choice=="4":
            print("bye")
            break
        else:
            print("invalid choice")

menu()

    

import sys
student = []

while True: 
    print("press 1 for add record")
    print("press 2 for display record")
    print("press 3 for count students")
    print("press 4 for delete last record")
    print("press 5 for Remove all records")
    print("press 0 for exit")
    ch = int(input("enter your choice "))
    if(ch == 1):
        rollNo = int(input("enter roll No: "))
        name = input("enter name: ")
        marks = int(input("enter marks: "))
        x = [rollNo, name, marks]

        student.append(x)
        print("record added")
    
    elif(ch == 2):
        for x in student:
            print(x)

    elif(ch == 3):
        print(len(student))

    elif(ch == 4):
        student.pop()

    elif(ch == 5):
        student.clear()

    elif(ch == 0):
        sys.exit()

    else:
        print("Invalid Choice")

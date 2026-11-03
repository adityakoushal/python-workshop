print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
a = int(input("enter first number: "))
b= int(input("enter second number: "))

ch = int(input("Enter your choice: "))

if(ch == 1):
        print("Addition is: ", a+b)
elif(ch == 2):
        print("Subtraction is: ", a-b)
elif(ch == 3):
        print("Multiplication is: ", a*b)
elif(ch == 4):
        print("Division is: ", a/b)
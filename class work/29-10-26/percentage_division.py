percentage = float(input("Enter the percentage: "))

if (percentage >= 60):
    print("Division I")
elif(percentage >= 45 and percentage < 60):
    print("Division II")
elif(percentage >=33 and percentage <= 45):
    print("Division III")
else:
    print("Fail")
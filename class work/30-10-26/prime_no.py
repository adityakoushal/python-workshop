num = int(input("Enter the number: "))

found = 0

for i in range(2, num):
    if(num % i == 0):
        found = 1
        break
if(found == 1):
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

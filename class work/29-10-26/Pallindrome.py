num = int(input("enter the number: "))

res = 0
temp = num

while(num != 0):
    a = num % 10
    res = (res * 10) + a
    num = num // 10
if(res == temp):
    print("Number is Pallindrome")

else:
    print("Number is not Pallindrome")
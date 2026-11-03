num = int(input("enter the number: "))
res = 0
temp = num

while(num != 0):
    a = num % 10
    res = res + (a ** 3)
    num = num // 10
if(res == temp):
    print("number is armstrong")
else:
    print("Number is not armstrong")

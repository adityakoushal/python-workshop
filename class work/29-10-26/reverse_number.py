num = int(input("enter the number: "))
res = 0
while(num!=0):
    a = num % 10
    res = (res * 10) + a
    num = num // 10
print("Reverse=",res)
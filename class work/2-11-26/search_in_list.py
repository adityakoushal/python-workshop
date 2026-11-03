
list = [2, 56, 7, 9, 10]
s = int(input("enter the number to be search: "))
found = 0
num = len(list)

for i in range(0, num):
    if(list[i] == s):
        found = 1
        break

if(found == 1):
    print("element found at",i+1,"position")
else:
    print("element not found")

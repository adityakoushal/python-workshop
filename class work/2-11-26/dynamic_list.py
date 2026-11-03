# program for dynamic list

a = [] #empty list 
num = int(input("enter the limit of list: "))

for i in range(0,num):
    data = int(input("enter new data: "))
    a.append(data)
print("list all data:",a)

for i in range(10):
    print(i, end=' ') #default it starts from 0 and goes up to 9
print()#it is used to print in a new line


for x in range(1,11):
    print(x, end=' ') #it starts from 1 and goes up to 10
print()#it is used to print in a new line


for i in range(2, 21, 2):
    print(i, end=' ') #it starts from 2 and goes up to 20 with a step of 2
print()


#break
for i in range(1, 11, 1):
    #if(i == 6):
    if(i == 6 and i == 8):
        break #it will break the loop when i is equal to 6
    print(i, end=' ')
print()
print("program is completed")

#continue
for i in range(1, 11, 1):
    if(i == 3 or i == 8):
        continue #it will skip the iteration when i is equal to 6
    print(i, end=' ')
print()
print("program is completed")

    
    
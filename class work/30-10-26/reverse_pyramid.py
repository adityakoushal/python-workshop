row = int(input("Enter the number of rows: "))
for i in range(row , 0, -1):
    for j in range(i, 0, -1 ):
        print("*", end=" ")
        #print(j, end=" ")
        #print(i, end=" ")
    print()
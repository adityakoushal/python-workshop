a = [34,40,342,329,484,42]
print("list before starting")
print(a)

# for no of rounds
for i in range(0,len(a)):
    for j in range(0,len(a) - 1 - i):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("list after sorting")
print(a)




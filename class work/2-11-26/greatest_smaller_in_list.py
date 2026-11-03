list = [2,45,23,65,43]
print(list)

max = list[0]
min = list[0]

for i in range(0, len(list)):
    if(list[i] > max):
        max = list[i]
    elif(list[i] < min):
        min = list[i]

print("maximum:", max)
print("minimum:",min)
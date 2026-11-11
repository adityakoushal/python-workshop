# slicing in list 
a = [10,20,30,40,50,60,70,80,90,100]
print(a)

print(a[0:5])
print(a[:6])
print(a[:10:2]) # skip element
print(a[-5:-1]) # reverse print
print(a[::]) #all data
print(a[::-1]) #reverse list
print(a[3:]) # 3 index to end of list
print(a[-9:-1])

del a[0:5]
print(a)
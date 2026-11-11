a = [10, 20, 30, 20, 50]
print(a)
b=[]

for x in a:
    if a.count(x) > 1 and x not in b:
        b.append(x)
print("element in list b")
print(b)
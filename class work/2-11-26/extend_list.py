a= [10,29,30]
b = [23, 34, 54]
a.extend(b)
print(a)

del a
print(a) # nameError: a is not defined
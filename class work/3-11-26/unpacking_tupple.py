#unpacking tupple 
name = ("Ram","Ritu","Shyam", "Ravi")#packing
print(name)
(x, *y, z) = name #unpacking
print(x)
print(y)
print(z)

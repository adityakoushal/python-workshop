a = 3
print(id(a))

b = 4
print(id(b))

res = a is b
print("Result:", res)

res = a is not b
print("Result:", res)

numbers = [10, 25, 5, 40, 30, 15]

first = second = float('-inf')

for i in numbers:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("First Maximum =", first)
print("Second Maximum =", second)

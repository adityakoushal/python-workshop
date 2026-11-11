a = (10, 20, 30)
print("Original tuple:", a)

# Tuples are immutable, so convert to a list before appending.
values = list(a)
values.append(60)
a = tuple(values)

print("Tuple after append:", a)

t = (10, 50, 20, 80, 30, 5)

maximum = t[0]
minimum = t[0]

for i in t:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum number =", maximum)
print("Minimum number =", minimum)
per = int(input("Enter the percentage: "))
year = int(input("Enter passing year: "))

#res = (per >= 75 and year >= 2024)
#res = (per >= 75 or year >= 2024)
res = not(per >= 75 and year >= 2024)
print("Result:", res)


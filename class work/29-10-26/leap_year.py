year = int(input("enter the year"))
# 400 4 100
if(year % 400 == 0 or year % 4 == 0):
    print("year is leap")

elif(year % 100 == 0):
    print("Not a leap year")

else:
    print("Not a leap year")
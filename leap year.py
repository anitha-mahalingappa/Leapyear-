year = int(input("enter the year"))

if year % 4 == 0 and year % 100 != 0:
    print (str(year) + "it's a leap year")
elif year % 400 == 0 or year % 100 != 0:
    print (str(year) + "it's a leap year")
elif year % 100 == 0:
    print (str(year) + "it's not a leap year")
else:
    print ("invalid year")    
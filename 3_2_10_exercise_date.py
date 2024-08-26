#Aufgabe 1: Tag

print("Please type in the day")

day = int(input())

print("Your day is:", day)

if day < 1 or day > 31:
    print("wrong date")


#Aufgabe 2,3,4: Monat

print("Please type in the month")

month = int(input())

print("Your month is:", month)

if month < 1 or month > 12:
    print("wrong date")
    
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Last day of the month is 31")

if month == 4 or month == 6 or month == 9 or month == 11:
    print("Last day of the month is 30")

if month == 2:
    print("Last day of the month is 28 or 29 when leapyear")
  
shortmonth = 2
mediummonth = 4 or 6 or 9 or 11
longmonth = 1 or 3 or 5 or 7 or 8 or 10 or 12

lastdayshortmonth = 28 or 29
lastdaymediummonth = 30
lastdaylongmonth = 31

if shortmonth and day < 1 or day > 29:
    print("wrong date")

elif mediummonth and day < 1 or day > 30:
    print("wrong date")

elif longmonth and day < 1 or day > 31:
    print("wrong date")


#Aufgabe 5,6: Jahr
    
print("Please type in the year")

year = int(input())

#modulo: % gibt den Restwert einer Ganzzahldiviosion aus, ist dieser gleich 0 gibt es keinen Rest!!!

print("Your year is:", year)

if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print("Leap year")
    
Leapyear = year%4==0
    
if shortmonth and day < 1 or day > 29 and not year % 4 == 0:
    print("wrong date")

elif mediummonth and day < 1 or day > 30:
    print("wrong date")

elif longmonth and day < 1 or day > 31:
    print("wrong date")

else:
    print("Right date")

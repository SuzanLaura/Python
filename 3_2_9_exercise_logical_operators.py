print("Please insert your monthly salary in euro:")

s = input()
salary = int(s)

print("Your salary is:",salary)

print("Please type in -1- for single or -2- for married:")

ms =input()
maritalsatus = int(ms)

single = 1
married = 2

print("You are single" if maritalsatus == 1 else "You are married")

bigtaxsingle = salary*0.26
bigtaxmarried = salary*0.22
smalltaxsingle = salary*0.22
smalltaxmarried = salary*0.18

if salary>4000 and maritalsatus == 1:
    print("There is a tax of",bigtaxsingle,"euro (single)")

if salary>4000 and maritalsatus == 2:
    print("There is a tax of",bigtaxmarried,"euro (married)")

if salary<=4000 and maritalsatus == 1:
    print("There is a tax of",smalltaxsingle,"euro (single)")

if salary<=4000 and maritalsatus == 2:
    print("There is a tax of",smalltaxmarried,"euro (married)")

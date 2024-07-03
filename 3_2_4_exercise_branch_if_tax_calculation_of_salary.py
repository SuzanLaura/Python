print("Please insert your monthly salary in euro:")

import random
random.seed()
x=random.randint(1000,9000)
number=x

print(number)

bigtax=number*0.22
smalltax=number*0.18

if number > 2500:
    print("There is a tax of",bigtax,"euro")

else:
    print("There is a tax of",smalltax,"euro")


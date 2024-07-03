import random
random.seed()

a=random.randint(1,10)
b=random.randint(1,10)
c=a+b

print(f"The task:{a}+{b}")

print("Please suggest a solution:")
number=int(input())

if number == c:
    print(number,"is right")

else:
    print(number,"is wrong")
    print("Result:",c)
    
    

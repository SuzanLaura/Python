import random
random.seed()

a=random.randint(1,10)
b=random.randint(1,10)
c=a+b

print(f"The task:{a}+{b}")

print("Please suggest a solution:")
number=int(input())
print("Your input:", number)
print("The result:", c)

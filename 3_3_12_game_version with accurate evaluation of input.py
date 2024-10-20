import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The task: {a} + {b}")

print("Please insert a soution:")

number = int(input())

if number == c:
    print(number, "is right")
elif number < 0 or number > 100:
    print(number," number is far off the mark")
elif c-1 <= number <= c+1:
    print(number, "is close")
else:
    print(number, "is wrong")

print("Result:", c)

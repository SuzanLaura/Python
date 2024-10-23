import random
random.seed()

x = random.randint(1,10)
print("x * 1.5 =", x * 1.5 )
match x * 1.5:
    case x if x < 5:
        print("small value")
    case x if x > 11:
        print("big value")
    case _:
        print("middle value")

print()

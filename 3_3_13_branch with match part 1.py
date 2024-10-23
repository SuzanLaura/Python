import random
random.seed()
x = "Paris"
match x:
    case "Paris":
        print("France")
    case "Rome":
        print("Italy")
    case "Madri":
        print("Spain")
    case _:
        print("unknown country")
        
print()

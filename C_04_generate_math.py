import random
import math



## Generate a number and square root it
# number2 = random.randint(1,100)
#
# x = math.sqrt(number2)
# x2 = math.floor(x)
# print(number2)
# print(x)
# print(x2)

# generate an equation and answer for pythagoras theorem

a = random.randint(1,10)
b = random.randint(1,10)
a2 = a*a
b2 = b*b

# print(a*a, "+",b*b)
eq = a2 + b2
ans = math.sqrt(eq)
ans2 = round(ans, 2)


# print(eq)
print(f"{a}² + {b}²")
print(f"Hint {ans}")
print(f"Hint {ans2}")
answer = float(input("answer? "))

if answer == ans2:
    print("You got it right!")
else:
    print("Too bad you got it wrong.")

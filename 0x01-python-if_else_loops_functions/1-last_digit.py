#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ldigit = abs(number) % 10
if number < 0:
    Ldigit = -Ldigit
print("Last digit of {} is {} and is ".format(number, Ldigit), end="")
if Ldigit > 5:
    print("greater than 5")
elif Ldigit == 0:
    print("0")
else:
    print("less than 6 and not 0")

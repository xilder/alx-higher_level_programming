#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    unit_digit = number % -10
else:
    unit_digit = number % 10
if unit_digit > 5:
    print(f"Last digit of {number} is {unit_digit} and is greater than 5")
elif unit_digit == 0:
    print(f"Last digit of {number} is {unit_digit} and is 0")
else:
    print(f"Last digit of {number} is {unit_digit} and is less than 6 and not 0")

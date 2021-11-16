#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
is_neg = False
if number < 0:
    number = number * -1
    is_neg = True
last_digit = number % 10
if is_neg:
    number = number * -1
if last_digit > 5:
    str = " and is greater than 5"
elif last_digit == 0:
    str = " and is 0"
elif last_digit < 6:
    str = " and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, last_digit, str))

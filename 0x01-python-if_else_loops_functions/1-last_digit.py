#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = abs(number) % 10
if number < 0:
    value = -value
if value > 5:
    print("Last digit of {} is {} {}".format(number, value, "and is greater than 5"))
elif value == 0:
    print("Last digit of {} is {} {}".format(number, value, "and is 0"))
else:
    print("Last digit of {} is {} {}".format(number, value, "and is less than 6 and not 0"))

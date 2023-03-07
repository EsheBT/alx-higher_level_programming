#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
module_value = number % 10
if number < 0:
    module_value = (-1 * number) % 10
    module_value *= -1
print("Last digit of {:d} is {:d}".format(number, module_value), end=" ")
if module_value > 5:
    print("and is greater than 5")
elif module_value == 0:
    print("and is 0")
elif module_value < 6 and module_value != 0:
    print("and is less than 6 and not 0")

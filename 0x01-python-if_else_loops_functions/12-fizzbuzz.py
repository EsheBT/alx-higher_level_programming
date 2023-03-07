#!/usr/bin/python3
def fizzbuzz():
    a = "Fizz"
    b = "Buzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{:s}{:s}".format(a, b), end=" ")
            continue
        if i % 3 == 0:
            print("{:s}".format(a), end=" ")
            continue
        if i % 5 == 0:
            print("{:s}".format(b), end=" ")
            continue
        print("{:d}".format(i), end=" ")

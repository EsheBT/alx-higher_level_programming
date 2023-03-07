#!/usr/bin/python3
def uppercase(str):
    index = 0
    while index < len(str):
        if ord(str[index]) >= ord('a') and ord(str[index]) <= ord('z'):
            tmp = chr(ord(str[index]) - 32)
        else:
            tmp = str[index]
        print("{:s}".format(tmp), end="")
        index += 1
    print()

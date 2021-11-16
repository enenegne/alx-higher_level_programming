#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i), end=" ")
        break
    if i <= 9:
        print("0{},".format(i), end=" ")
    else:
        print("{},".format(i), end=" ")

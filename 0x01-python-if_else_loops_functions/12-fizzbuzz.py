#!/usr/bin/python3

def fizzbuzz():
    """
    FIZZ BUZZ
    """
    for i in range(1, 101):
        if 1 % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(i), end=" ")

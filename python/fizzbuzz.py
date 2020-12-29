"""
Author:         Bill Li
Description:    FizzBuzz is a coding problem where a program takes in an integer and
                returns "Fizz" if it is evenly divisible by 3
                        "Buzz" if it is evenly divisible by 5
                        "FizzBuzz" if it is is evenly divisible by 3 and 5
                        Otherwise it returns the number
"""


def fizzbuzz(num: int):
    for i in range(1, num+1):
        if i == 1:
            print(1)
        if i == 2:
            print(2)
        if i == 3:
            print("Fizz")
        if i == 4:
            print(4)
        if i == 5:
            print("Buzz")
        if i == 6:
            print("Fizz")
        if i == 7:
            print(7)
        if i == 8:
            print(8)
        if i == 9:
            print("Fizz")
        if i == 10:
            print("Buzz")
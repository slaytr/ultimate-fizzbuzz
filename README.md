# Ultimate FizzBuzz

FizzBuzz is a program that prints the numbers from 1 onwards. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

###
This repository is updated daily and adds support for 10 integers each night, if your number is not supported yet.
Be patient and wait a few days.

### Example
```
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
```
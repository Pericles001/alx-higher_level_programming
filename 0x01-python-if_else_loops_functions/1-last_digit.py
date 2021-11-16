#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10

if digit > 5 :
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0 :
    print("Last digit of {} is {} and is zero".format(number, digit)) 
else :
    print("Last digit of {} is {} and is less than 6 and not zero".format(number, digit))


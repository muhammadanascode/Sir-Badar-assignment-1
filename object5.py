# Write a program that takes input an integer number and print all of its Divisors.

import math

num = int(input("Enter a number to find all divisors"))
x = math.ceil(num/2) + 1
for i in range(1, x):
    if (num % i == 0):
        print(f"{i} is a divisor of {num}")

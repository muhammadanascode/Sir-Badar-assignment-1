# Write a program that takes input two integer numbers and prints all the common divisors.

num1 = int((input("Enter a 1st number: \n")))
num2 = int(input("Enter a sceond number: \n"))

if (num1 == 0 or num2 == 0):
    print("Enter a number greater than 0")

else:
    x = num1 if num1 < num2 else num2
    for i in range(1, x+1):
        if (num1 % i == 0 and num2 % i == 0):
            print(f"{i} is a common divisor of {num1}  and {num2}")

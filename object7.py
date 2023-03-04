# Extend the logic of last object to write a program that takes input two integer numbers and print highest common divisor

num1 = int((input("Enter a 1st number: \n")))
num2 = int(input("Enter a sceond number: \n"))
hcf = 0

x = num1 if num1 < num2 else num2
for i in range(1, x+1):
    if (num1 % i == 0 and num2 % i == 0):
        hcf = i

print(f"The hcf of a {num1} and {num2} is {hcf}")
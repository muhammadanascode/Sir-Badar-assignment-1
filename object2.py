# Write a program that prints Factorial of a user given integer without using math.factorial()

num = int(input("Enter a number to find factorial: \n"))
factorial = 1

if(num<0):
    print("Enter a postive integer")

else:
    for i in range(num, 1, -1):
        factorial *= i
    print(f"The factorial of a number is {factorial}")

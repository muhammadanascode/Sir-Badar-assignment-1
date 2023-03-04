# Write a Python program to find numbers between 100 and 400 (both included) where each digit
# of a number is an even number. The numbers obtained should be printed in a comma-separated
# sequence

print("The series is given which contain all even number between 100 and 400 are:\n")
for num in range(100, 401):
    a = str(num)
    if (int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0 and int(a[2]) % 2 == 0 ):
        print(int(a))

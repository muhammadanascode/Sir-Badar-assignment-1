# Write a Python program to find numbers between 100 and 400 (both included) where each digit
# of a number is an even number. The numbers obtained should be printed in a comma-separated
# sequence

li = []

for num in range(100, 401):
    c = ""
    a = [int(i) for i in str(num)]
    if ((a[0] % 2 == 0 or a[0] % 2 == 2) and (a[1] % 2 == 0 or a[1] % 2 == 2) and (a[2] % 2 == 0 or a[2] % 2 == 2)):
        for j in a:
            c += str(j)
        print(int(c))

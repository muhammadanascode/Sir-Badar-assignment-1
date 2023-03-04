# Take two inputs from user and print all the number b/w them seq as quest two if user gives 16 and 20 it must gives error

x = int(input("Enter the first number of a range:\n"))
y = int(input("Enter the second number of a range:\n"))
c = False

for i in range(1,10):
    a = i*i-1
    for j in range(x,y+1):
        if(a == j):
            print(f"The range contains {j}")
            c = True

if(c == False):
    raise Exception(f"No number lies between {x} and {y}")



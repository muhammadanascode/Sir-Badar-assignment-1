# Take two inputs from user and check the an number of series lies between given inputs 


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
    print(f"No number lies between {x} and {y}")



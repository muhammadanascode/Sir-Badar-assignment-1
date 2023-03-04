#Taking two number input from user and priniting all the odd numbers between them

num1 = int(input("Enter a first number: \n"))
num2 = int(input("Enter a second number: \n"))

x  = num1 if num1<num2 else num2
y = num1 if num1>num2 else num2

for i in range(x,y+1):
    if(i%2 != 0):
        print(f"{i} is a odd number")
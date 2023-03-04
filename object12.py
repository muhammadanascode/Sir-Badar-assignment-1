# find Lcm by relation lcm = a*b/gcd

num1  = int(input("Enter a first number: \n"))
num2  = int(input("Enter a second number: \n"))
x  = num1 if num1<num2 else num2
gcd = 0

for i in range(1,x+1):
    if(num1%i == 0 and num2%i == 0):
        gcd = i

lcm = num1 * num2 / gcd
print(lcm)

# a)Take two number input from a user and print HCF by process
#  b) assign smaller number in variable s and greater number in variable g
#  c) r = g%s if r = 0 then assign smaller number in GCD 
#  d)  if r != 0 then assign smaller s in g and remainder r in s

num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter first number: \n"))
s = num1 if num1<num2 else num2 
hcf = 0
gcd = 0

for i in range(1 , s+1):
    if(num1%i == 0  and num2%i == 0):
        hcf  = i
print(hcf)
g = num1 if num1>num2 else num2
r = g%s
if(r == 0):
  gcd = s
  print(gcd)

else:
   s,r = g,s
   print(s,r)




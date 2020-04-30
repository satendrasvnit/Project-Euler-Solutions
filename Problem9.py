# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
a=1
b=1
c=1
num=int(input("Enter the number..."))
for a in range(1,math.floor(num/3)):
    for b in range(1,math.floor(num/2)):
        c=num-a-b
        if c<0:
            break
        if (a*a+b*b-c*c)==0:
            print("The Triplet is",a,b,c)
            product=a*b*c
print("The product of the Triplet is :",product)

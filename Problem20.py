# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def findFact(num):
    num=num+1
    factorail=1
    for i in range(1,num):
        factorail*=i
    return factorail

def sumofdigits(num):
    total=0
    while(num!=0):
        total=total+num%10
        num=num//10
    return total


num=int(input("Eneter the number:.."))
num=findFact(num)
print(sumofdigits(num))

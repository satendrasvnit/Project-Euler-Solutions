# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

n=2**1000
print(n)
sum=0
while(n>0):
    sum=sum+n%10
    n=int(n//10)

print(sum)

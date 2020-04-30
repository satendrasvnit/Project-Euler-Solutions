# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

num=10000000
length=1
def isprime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=0
            break
        else:
            flag=1
    return flag

for i in range(1,num):
    flag=isprime(i)
    if flag==1:
        length+=1
    if length>=10001:
        print(i)
        break

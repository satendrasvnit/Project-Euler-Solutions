#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#There are many methods to solve this. The easiest method is just
#check all the number if it is prime or not, if its prime check divisibility
#But it not really a smart method,

#METHOD-1
# num=600851475143
# largest=1
# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             flag=0
#             break
#         else:
#             flag=1
#     return flag
#
# for i in range(3,num):
#     if isprime(i) ==1:
#         if num%i==0:
#             largest=i
# print(largest)


#MTHOD-2
#Mthod 2 Fast method
#First we will find firt 100000 prime numbers
flag=0
primelist=[]
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            flag=0
            break
        else:
            flag=1
    return flag

for i in range(3,10000):
    if isprime(i)==1:
        primelist.append(i)

largest=0
num=600851475143
for i in primelist:
    if num%i==0:
        largest=i
print("Larget prime factor",largest)

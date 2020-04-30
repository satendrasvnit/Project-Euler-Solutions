# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisibility(num):
    flag=0
    if num%11==0 and num%12==0 and num%13==0 and num%14==0 and num%15==0 and num%16==0 and num%17==0 and num%18==0 and num%19==0 and num%20==0:
        flag=1
    return flag
i=1
while True:
    i+=1
    flag=0
    flag=divisibility(i)
    if flag==1:
        print("Smallest divisible number is: ",i)
        break

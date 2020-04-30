#Problem If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
sum3=0
sum5=0
for i in range(3,999):
    if i%3==0:
        sum3+=i
    elif i%5==0:
        sum5+=i
print(sum3+sum5)

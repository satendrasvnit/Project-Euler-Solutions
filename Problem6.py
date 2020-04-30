# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
num=int(input("Enter the Number limit..."))
choice=int(input("Enter 1 for Hard Method\nEnter 2 for Easy Method"))
if choice ==1:
    sumofSq=0
    sqofsum=0
    for i in range(1,num+1):
        sqofsum+=i
        sumofSq=sumofSq+i*i
    sqofsum=sqofsum*sqofsum
    print(sumofSq)
    print(sqofsum)
    print("difference:", sqofsum-sumofSq)
if choice==2:
    sum=(num)*(num+1)/2
    sqofsum=sum*sum
    sumofSq=(num)*(num+1)*(2*num+1)/6
    print("difference:", sqofsum-sumofSq)

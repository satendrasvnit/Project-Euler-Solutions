# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#Srategy: Loop starts from larget number and gets multiplied by all the nubmers
#till 100. In inner loop the number will be varified by the product of last numbers
#if it is greater than the last palnidrom number, it will be updated
#to reverse the paneldrom, first the number will be converted into a starting
#then this strin will be reversed using [::-1] property. If comparission is successful
#the nubmer will get stroed as the biggest known palindrome
num=int(input("Enter the NUMBER:..."))
largestPalindrom=0
for i in range(num,100,-1):
    for m in range(i,100,-1):
        product=i*m
        if product>largestPalindrom:
            s=str(product)
            if s==s[::-1]:
                largestPalindrom=i*m
print(largestPalindrom)

temp=0
def isprime(n,temp):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n):
        if prime[p]:
            print(p)
            temp+=p
    return temp
n=int(input("Enter the number:..."))
print("Following are the prime nubmers smaller that",n)
temp=isprime(n,temp)
print("Total: ",temp)

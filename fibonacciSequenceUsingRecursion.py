def fibonacci(n):
    #base case
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
n=int(input("enter the n:"))
for i in range(1,n+1):
    print(fibonacci(i))
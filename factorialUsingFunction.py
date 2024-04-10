def factorial(n):
    pro=1
    if n==0:
        return 1
        pro=1
    else:
        for i in range(1,n+1):
            pro*=i
    return pro
n=int(input("enter n:"))
result=factorial(n)
print("factorial is:",result)
      
#factorial using recursion
def factorial(n):
    #base case
    if n==0:
        return 1
    #recursive case
    fact=n*factorial(n-1)
    return fact

n=int(input("enter the number :"))
print(factorial(n))
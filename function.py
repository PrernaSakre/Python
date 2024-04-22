#to print hello world
def function():
    print("hello prerna!!")
function()


#take two numbers as input and find their sum
def add(n1=0,n2=0):
    print("n1:",n1)
    print("n2:",n2)
    sum=n1+n2
    return sum

n1=5
n2=5
print("the sum is:",add(n1,n2))


#positional argunmengtpp
print("the sum is:",add(5,3))

#keyword argunment
print("the sum is:",add(n2=5,n1=6))

#default argunment
print("the sum is:",add())

#arbitrary argunment
def addAllNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
    
output = addAllNumbers(16,26,35,44,52,65,7,8)
print("the sum is:",output)
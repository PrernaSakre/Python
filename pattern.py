n=int(input("enter the number of term:"))
for n in range(n):
    print(" *"*4)

#program for print number in square pattern
n=int(input("enter the number of term:"))
for i in range(n):
    for j in range(1,n+1):
        print(" ",j, end=" ")
    print()

#program for print the half pyramid
n=int(input("enter the number of term:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(  j, end=" ")
    print()

#program for print the full pyramid
n=int(input("enter the number of term:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
            print(j,end="")
    print()






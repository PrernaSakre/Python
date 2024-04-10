num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operator=input("enter operator:")

match operator:
    case "+":
        print("sum is",num1+num2)
    case "-":
        print("subtraction is",num1-num2)
    case "*":
        print("multiplication is",num1*num2)
    case "/":
        print("division is ",num1/num2)
    case _:
        print("enter a valid operator")
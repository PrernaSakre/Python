#pass by value
def sum_num(x):
    x=x+1
    print("inside the function:",x)

x=6
sum_num(x)
print("outside the function:",x)






#pass by reference
def new_list(list):
    list.append(65)
    print("inside the function:",list)

list=[5,25,62,78]
new_list(list)
print("outside the function:",list)


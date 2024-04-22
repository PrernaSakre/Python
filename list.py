number=[23,54,67,98,4,8,56,45]
print(number)
number[4]=56
print(number)
print(type(number))
print(len(number))

#access the list
print(number[-2])
print(number[1:4])
print(number[-3:-1])
n=int(input("enter a number"))
if n in number:
    print(n, "is a part of list")
else:
    print(n,"is not present in list")



list=[1,2,3,4,5,6,7,8]
new_list=list[:]
new_list.append(9)
print(list) 
print(new_list)


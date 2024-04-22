colour=("red",'a',"green",2.13,"pink","blue")
#type 
print(type(colour))
#length
print(len(colour))


#accessing the tuple
print(colour[1])
print(colour[1::])
print(colour[-5:-1])

n=str(input("enter a colour"))
if n in colour:
    print(n," is part of a tuple")
else:
    print(n," is not part of a tuple")


#add extra elements in tuple
new_colour=("black","white","silver","golden")
colour=colour+new_colour
print(colour)


#reverse of tuple
i_tuple=(10,20,30,40,50,60)
list= []
for x in reversed(i_tuple):
    list.append(x)
new_tuple = tuple(list)
print(new_tuple)
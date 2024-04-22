name='I Am Prerna'
name1="sakre"
name2=''' and
who
are
you?'''
print(name,name1,name2)
print(type(name2))
print(len(name2))
print(name[5])

#traversing a string
for i in name:
    print(i)

#find a character in string
print("k is present in index:",name1.find('k'))

print(name.lower())
print(name.upper())

#upper
list="i am ashu"
list1=list.upper()
print(list1)

#lower   
list2=list1.lower()
print(list2)

#capitalising first character of string
list3=list2.capitalize()
print(list3)

#for stripping/removing any trailing whitespace 
str="     i am rishi     "
str1=str.strip()
print(str1)

#replace
str="i am rishi ,i am fine"
str1=str.replace("rishi","prerna",1)#count is not neccessery
print(str1)
  
#splitting
str="ria,pia,sia,mia,jia"
str1=str.split(",", 2)
print(str1)

#concatenation of string
str1="i am pranay"
str2=" i am 10years old"
print(str1+str2)

#formating a string
colour1="green"
colour2="orange"
colour="i have two colour {c1},and {c2}".format(c1=colour1,c2=colour2)
print(colour)




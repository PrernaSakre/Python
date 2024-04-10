phones= {
    "ashu" :9926731196,
    "prerna" : 9303946824,
    "pranay" : 9575412730,
    "papa" : 7974129883
}
print(type(phones))    #type
print(len(phones))     #to find the length
print(phones["ashu"])   #to find the value of given key
print(phones.get("prerna"))    #it is also used to get the value of a key
print(phones.keys())        #to print all keys present in dictionary
print(phones.values())       #to print all values 
print("the sum of all key value is: ",sum(phones.values()))     


 
#change the value
phones["ashu"]=7828183347
print(phones)

#add new keys and value
phones["ria"]=9098923751
print(phones)

#add a new dictionary to old dictionary
phones_1={
    "ram":56895213,
    "krish":13743242,
    "jay":13456231453
}
phones.update(phones_1)
print(phones)

#remove a key value
phones.pop("ashu")
print(phones)

#remove last key value
phones.popitem()
print(phones)

#empty the dictionary
phones.clear()
print(phones.items())

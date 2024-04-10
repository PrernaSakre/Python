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



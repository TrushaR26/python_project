tinydict = {'name':'john','code':'6374','dept':'sales'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dict1 ={ 1:["trusha","ruparelia"],2:" infividhya",3:"dharti"}
print(dict1)
print(dict1.get(1))
#print(dict1.clear())
#print (dict1)

#add an key element to the dictionary

dict1[4]="priya"
print(dict1)

#update in dictionary
dict1.update({2:"gujarat university"})
print(dict1)

print(type(dict1))
# fetch from particular key
print(dict1[1])

#items in dictionary

print(dict1.items())

# using dict function  make  dictionary
gala =dict(name="trusha",floor=7, no=727)
print(gala)
print(type(gala))
print(gala["floor"])
gala.update({"name":" dharti"})
print(gala)


if "name"in gala:
    print("yes it is key in dict")
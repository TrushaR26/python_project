#find id  of variable
a="may"
b=id(a)
print(b)

trusha = "trusha"
print(trusha)

# to delete any variable use function del
#del trusha
#print(trusha)

# to check type of varible whether string float
a=type(trusha)
print(a)

b=2.3
c=type(b)
print(c)

may=10
print(type(may))

#tqw=(input("enter value:"))
#print(tqw)

#casting variables i.e. to change data type of a variable


rup = 2.3
x=str(rup) # will cgange var to string variable
y=int(rup)
z=float(rup)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#case sensitive
X= 20
print(X)
print(x)
P=10
Q=10
R=10
print(P,Q,R)
P=Q=R=20
print(P,Q,R)

abc,pqr,xyz=10,2.6,"trusha"
print(abc,pqr,xyz)
var1=True
print(type(var1))
var2= 10+3j
print(type(var2))

#string operations
efg=" HELLO WORLD "
print(efg[0:3])
print(efg[0])
print(efg[1:6])
print(efg[1:])
print(efg*3)
print(efg+"you are ready")
print(efg[:12])

#list operations
list= [1,2.3,"trusha",4+3j]
print(list)
print(type(list))
print(list[0])
print(list[1:])
print(list*2)
print(list + ["dharti",2,5.6])
list2=[1,2,3,4]
list3=[4,5,6,7]
print(list2[0:4]+list3[0:4])
list[0:2]=4,6
print(list)
list[0:3]=4,6,8,9,10,16
print(list)
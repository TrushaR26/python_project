i=0
j=0

for i in range (0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
print("\n")

for i in range (0,5):
    for j in range(0,i+1):
        print("1",end=" ")
    print("\r")
print("\n")


no=0
for i in range (0,5):
    for j in range(i):
         print(no*i,end=" ")
         no+=1
    print("\r")

for i in range(1,6):
    print(" "*(5-i)+"* "*i,end=" ")
    print()

txt="the string is free"
print("alpa"  not in txt)


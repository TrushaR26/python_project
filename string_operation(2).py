age=36
txt=("my name is john,I am {}")
print(txt.format(age))

txt2=("my name is john,I am" + str(age))
print(txt2)

quantity=3
itemno=567
price=49.95
myorder="I want {2} pieces of item {0} for {1} dollars. "
print(myorder.format(itemno,quantity,price))
#format is used to specify in between txt

txt="the string \fvvvv is free"
print( txt)

x=3
y=4
print(x^y)
print(x+y)

a=" Hell o ,world "
print(a.upper())
print(a.lower())
print(a.strip())
#strip only removes spaces in front and back
print(a.split(","))

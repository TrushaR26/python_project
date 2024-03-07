p=int(input("Enter principal amount:"))
r= int(input("Enter Rate of interest:"))
t= int(input("enter no of years: "))
n=int(input("enter no of times the interest should be  compounded "))
simpleinterest = (p*r*t)/100
print(simpleinterest)
print("simple interest= ", simpleinterest)

ci=(p*(1+(r*t/n))**n*t)-p
print(" compound interest= ", ci)

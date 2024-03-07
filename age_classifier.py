age= int(input("Enter age:"))

if 0<=age<=12:
    print("The person is included in  child category")
elif 13<= age <=19:
    print("The person is included in  teenage category")
elif 20 <= age <=59:
    print("The person is included in  adult category")
else:
    print("The person is included in  senior citizen category")


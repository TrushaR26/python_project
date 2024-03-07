n=int(input("enter number:"))
def prime(n):
    i=2
    if i < n and n % i == 0:
        return "the no is not  prime"
    else:
        return "the no is prime"

output = prime(n)
print(output)
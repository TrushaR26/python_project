
#n=int(input("enter number"))
#def factorial(n):
 #   result = 1
  #  for i in range (n+1):
   #      if n-i !=0:
    #        result=result*n*(n-1)
     #    n = n-2

    #return result
#output=factorial(n)
#print(output)

n=int(input("enter digit:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        result= n * factorial(n-1)
        print(result)
        return result

output=factorial(n)
print(output)
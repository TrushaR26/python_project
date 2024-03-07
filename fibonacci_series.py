#para1=0
#para2=0
#result=0
#def fibo(para1,para2):
    #result=para1+para2
    #return result

#for i in range(1,100):
    #output=fibo(i, i+1)
    #i=i+1
    #j=i+1
    #j=result

def fibo(n):
    fibo_seq=[0,1]
    while(len(fibo_seq))<n:
        fibo_seq.append(fibo_seq[-1]+fibo_seq[-2])
    return fibo_seq

result=fibo(8)
print(result)
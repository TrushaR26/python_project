import numpy as np

a=np.array([10,20,30,40])
b=np.array([50, 40,70,80])
result=np.union1d(a,b)
print(result)
result2=np.intersect1d(a,b)
print(result2)

data=np.array([5,10,15,20])
bin=[0,10,20,30]
graph= np.histogram(data,bin)
print(graph)



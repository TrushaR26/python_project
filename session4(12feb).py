#library using python
#numpy
import numpy as np
list1 = [2,4,6,8]
array1= np.array(list1)
print(array1)

#directly elemts in np.array
array2=np.array([2,4,"trur",8])
print(array2)
array3=np.zeros(4)
print(array3)
array4=np.ones(6)
print(array4)

array5 =np.arange(1,9,2)
print(array5)

array6=np.arange(5)
print(array6)
#create random numbers
array7 = np.random.rand(5)
print(array7)

#create empty array with garbage value
array8 = np.empty(4)
print(array8)

#create 2 dimensional array
array9 = np.array([[1,2,3,4],[5,6,7,8]])
print(array9)

array10 = np.array([[1,2,3,4],[5,6,7],[8]])
print(array10)

array11 = np.array([[[1,2,3,4],[5,6,7,8],[10,11,12,13]],[[14,15,16,17],[18,19,20,21],[22,23,24,25]]])
print(array11)

shape=np.shape(array11)
print(shape)

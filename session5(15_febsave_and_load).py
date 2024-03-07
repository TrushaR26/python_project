import numpy as np
array1= np.array([[1,2,3,4],[5,6,7,8]])
np.save("file.npy",array1)

array2= np.load("file.npy")
print(array2)

np.savetxt("file2.txt",array1)
array3=np.loadtxt("file2.txt")
print(array3)


#indexing of elements in array
#array[start:stop:increment]
array4=np.array([1,2,3,4])
print(array4[1])
array5=np.array([[1,2,3,4],[5,6,7,8]])
print(array5[0,3])
array4[1]=5
print(array4)
array5[0,3]=7
print(array5)
array5[0,3],array5[1,3]=10,11
print(array5)
print(array4[-2])
array4[-1]=6
print(array4)
array5=np.array([[[1,2,3,4],[5,6,7,8],[10,11,12,13]],[[14,15,16,17],[18,19,20,21],[22,23,24,25]]])
print(array5[1,0,1])
array5[1,2,0]=50
print(array5)

#19thfeb
array6=np.array([[1,3,5],[7,9,2],[4,6,8]])
print(array6[1,:])
print(array6[:,2])
print(array6[1,1])
array7=np.array([2,4,6,8,10,12])
array7[3:]=12
print(array7)#will change all elements after index3
array7[:3]=16
print(array7)#will change all elements till index 3
#with increment of two
array7[1:5:2]=3
print(array7)
#using negative indexing
print(array7[-2:-6:-1])
array8=np.array([[1,3,5],[7,9,2],[4,6,8]])
print(array8[1:3,:])
print(array8[1:3:2,0:1])
print(array8[1:3:2,0:1:2])

#3D array
array9=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(array9[1,2,1])
array9[1,0]=20
print(array9)
array9[1,0]=[20,81,91,71]
print(array9)



#1)create 1D array  with elements 1to10
import numpy as np
array1=np.arange(1,11)
print(array1)

#2)create a 2d array  shape(3,4)
array2= np.random.rand(3,4)
print(array2)
print(array2.ndim)

#3)perform element wise add,sub,multiply,division on two array
array12=np.arange(1,6)
array21=np.arange(12,17)

add_array=np.add(array21,array12)
print("addition",add_array)
sub_array=np.subtract(array12,array21)
print("subtract",sub_array)
multiply_array=np.multiply(array12,array21)
print("multiply",multiply_array)
divide_array=np.divide(array12,array21)
print("divide",divide_array)



#even indices  from 1d array
array3=np.array([2,5,67,87,45,7,4])
print(array3[1::2])
print(array1[1::2])
array4=np.arange(1,12,2)
print(array4)

#ques5 create a 2d array and fetch 2st row and 3rd column
array5= np.array([[1,3,5],[7,9,2],[4,6,8]])
print(array5[1])
print(array5[0:3,2:])

#ques6 create a 3d array and  get array elements [1,2,1]
array6=np.random.rand(2,3,4)
print(array6)
print(array6.ndim)
print(array6[1,2,1])

#ques7 save array in txt file
np.savetxt("array_save.txt",array5)

#ques 8 load ques in numpy array
array7=np.loadtxt("array_save.txt")
print(array7)

#ques9 marksheet calculate percentage and rank max as 1st

#marksheet=np.array([["roll no","name","sci","maths","eng"],[1,"a",45,56,78],[2,"b",67,78,79],[3,"c",86,89,86]])
#print(marksheet)
#for i in range (1,2):
#    total=np.add(marksheet[i,2:])
#   print(total)
eng=np.array([56,67,78,89,89])
science=np.array([34,23,34,56,78])
maths=np.array([56,89,56,59,89])
computer=np.array([89,65,89,52,63])
ss=np.array([96,56,85,75,86])
add_array=eng+science+maths+computer+ss
percentage=add_array/500*100

print(add_array)
print(percentage)
print("student with rank1 and percentage",np.max(percentage))

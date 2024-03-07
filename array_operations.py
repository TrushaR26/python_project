import numpy as np

array1=np.array([1,2,3,4])
array2=np.array([5,10,7,8])
#addition

add_result=array1+array2
add2result=np.add(array1,array2)
print("add",add_result)
print(add2result)

#subtract
sub_result=array1-array2
sub_result2=np.subtract(array1,array2)
print("subtract",sub_result)
print(sub_result2)

#multiply
multiply_result = array1*array2
multiply_result2=np.multiply(array1,array2)
print("multiply",multiply_result)
print(multiply_result2)

#divide
divide_result =array1/array2
divide_result2 =np.divide(array1,array2)
print("divide",divide_result)
print(divide_result2)

#power
power_result = array1**array2
power_result2 =np.power(array1,array2)
print("power",power_result)
print(power_result2)

#modulo
modulo_result=array2%array1
modulo_result2=np.mod(array2,array1)
print("modulo",modulo_result)
print(modulo_result2)

#ststistical functions

marks=np.array([76,78,79,81,81,99,90,91,56,64])
mean_marks=np.mean(marks)
print("mean",mean_marks)

median_marks =np.median(marks)
print("median",median_marks)

#mode_marks=np.mode(marks)
#print("mode",mode_marks)

std_dev_marks=np.std(marks)
print("std dev",std_dev_marks)

variance_marks=np.var(marks)
print("variance",variance_marks)

min_marks=np.min(marks)
print("min marks",min_marks)

max_marks=np.max(marks)
print("max marks",max_marks)

array3=np.array([1,2,3,8,5])
array4=np.array([5,6,7,4,5])

#logical operators
#less than
print("less",array3<array4)
less_aray=np.less(array3,array4)
print(less_aray)

#lessthan equal
print("less than equal",array3<=array4)
less_equal_aray=np.less_equal(array3,array4)
print(less_equal_aray)

#greater
print("greater",array3>array4)
greater_aray=np.greater(array3,array4)
print(greater_aray)

#greaterthan equal
print("greaterthan equal",array3>=array4)
greater_equal_aray=np.greater_equal(array3,array4)
print(greater_equal_aray)

#equal
print("equal",array3==array4)
equal_aray=np.equal(array3,array4)
print(equal_aray)

#notequal
print(" not equal",array3!=array4)
not_equal_aray=np.not_equal(array3,array4)
print(not_equal_aray)






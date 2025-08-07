import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# 0D Array
a = np.array(41)
print(a) #41
print(a.ndim) # 0 => TO check dimentions
print("---------------------------")


# 1D Array
b = np.array([1,2,3,4,5])
print("Array : ", b)
print("Dimension : ", b.ndim) # 1
print("First element from the array : ", b[0])
print("Slicing b[1:2] is ", b[1:3])
print("Slicing with step b[1:5:2] is ", b[1:5:2])
print("Slicing with step b[::2] is ", b[::2])
print("---------------------------")


# 2D Array
c = np.array([[1,2,3], [4,5,6]])
print(c)
print(c.ndim) # 2
print("First row 3rd element", c[0,2]) # 3
print("Last element from first row", c[1,-1]) # 6
print("Slicing and get index element c[0:2, 2]", c[0:2, 2]) # [3 6]
print("Slicing and get sliced element c[0:2, 1:2]", c[0:2, 1:2]) # [[2] [5]]
print("---------------------------")


#3D Array => two 2D arrays
d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(d)
print(d.ndim) # 3
print("First array : second row :  second element", d[0, 1, 1]) # 5
print("Second array : second row :  First element", d[1, 1, 0]) # 10
print("---------------------------")

#Higher dimensional array
e = np.array([1,2,3,4,5], ndmin = 5)
print(e)
print(e.ndim)
print("---------------------------")



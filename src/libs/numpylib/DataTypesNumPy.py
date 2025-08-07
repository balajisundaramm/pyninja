import numpy as np

# 11 data types

a = np.array([1,2,3,4,5])
print("Datatype of the array : ", a.dtype) # int 64
print("=====================================")

a = np.array(["apple", "banana"])
print("Datatype of the array : ", a.dtype) # <U6
print("=====================================")

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
print("=====================================")

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
print("=====================================")

# arr = np.array(['a', '2', '3'], dtype='i') # value error
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype) # int 32
print("=====================================")


arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype) #int 64
print("=====================================")

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print("=====================================")


# Copy Vs View
# Copy owns the data (base) view refers to the original

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) # Changed value 42
print(x) # Original value
print("=====================================")

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr) # Updated value
print(x) # Updated value
print("=====================================")


arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) # None
print(y.base) # Refers to the original
print("=====================================")
#Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # 2,4 2*4 matrix
print("=====================================")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape) # 1,1,1,1,4
print("=====================================")
#Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr) # [[[1,2,3] [4,5,6] [7,8,9] [10,11,12]]
print("=====================================")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr) # [[[1,2] [3,4] [5,6]] [[7,8][9,10][11,12]]]
print("Base of the array : ", newarr.base)
print("=====================================")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr) # [1,2,3,4,5,6]
print("=====================================")
#Iteration
newarr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(newarr):
    print(x)   # Flatten the array and print
print("=====================================")
# Change the datatype of the element=
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x) # b'1' b'2' b'3'
print("=====================================")
#Iterating with different steps
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
for x in np.nditer(arr[:]):
    print(x)
print("=====================================")
# 2D Array 2*4 matrix
# First Colon array slicing here all the rows
# Every second column starting from 0 (0th and 2nd) (1 3 5 7)
for x in np.nditer(arr[:, ::2]):
    print(x)  # 1 3 5 7
print("=====================================")
# First : slices the row starting from 1st index (5 6 7 8)
# Second : slices the elements from 0 to 2 exclusive index (5 6)
for x in np.nditer(arr[1:, :2]):
    print(x) # 5, 6
print("=====================================")
# First : slices the row starting from 1st index (5 6 7 8)
# Second : slices the elements from 1 to 3 exclusive index (6,7) and skip the alternative character
for x in np.nditer(arr[1:, 1:3:2]):
    print(x) # 6
print("=====================================")
#Get the index while iterating
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print("=====================================")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
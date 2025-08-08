import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print("=====================================")
# axis 0 means Vertical stacking (along rows) Columns must match
# we have 2*2 matrix, it stacks the arrays in rows,
# we will have 4*2 matrix
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
print("=====================================")
# axis 1 means horizontal stacking, it stacks the arrays in columns
# Rows must match
# we have 2*2 matrix, output is 2*4 matrix
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print("=====================================")
arr1 = np.array([1, 2, 3, 4, 5]) # shape (5,)
arr2 = np.array([6, 7, 8, 9, 10])# shape (5,)
arr = np.stack((arr1, arr2), axis=0)
# Joining by stack means it adds the new array in new axis.
# New axis is added at position 0
# We will get 2*5 matrix [[1,2,3,4,5], [6,7,8,9,10]]
print(arr)
print("=====================================")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
# Joining by stack means it adds the new array in new axis.
# New axis is added at position 1
# We will get 5*2 matrix [[1,6], [2,7], [3,8], [4,9], [5,10]]
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print("=====================================")
# Stack along rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr) # [1,2,3,4,5,6]
print("=====================================")
# Stack along columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr) # [[1,2,3],[4,5,6]]
print("=====================================")
# Stack along Height (Depth)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr) # [[1,4],[2,5],[3,6]]]
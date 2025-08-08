import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) # [1,2][3,4][5,6]
# Splits the array to the mentioned number of sections either equally or unequally
print("=====================================")
newarr = np.array_split(arr, 4)
print(newarr) # [1,2][3,4][5][6]
# Splits the array to the mentioned number of sections either equally or unequally
# 6/4 = 1 => each section will have minimum one element
# 6%4 = 2 => equally distributed into first 2 sections
print("=====================================")
# 6*2 matrix
# 3 sections 2*2 matrix
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(arr)
newarr = np.array_split(arr, 3)
print(newarr) #[[1,2][3,4]]  #[[5,6][7,8]]  #[[9,10][11,12]]
print("=====================================")
# 6*2 matrix
# 6/4 => 1 => each will have 1 element
# 6%4 => 2 => first 2 will have 2 elements
# 2*2 => 2 => [[1,2][3,4]]  [[5,6][7,8]]
# 1*2 => 2 => [9,10]  [11,12]
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 4)
print(newarr)
print("=====================================")
#Split by columns
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr) # [1,4,7,10,13,16] [2,5....] [3,6,...]
print("=====================================")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr) # [1,4,7,10,13,16] [2,5....] [3,6,...]
print("=====================================")
# Split by Rows V split
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.vsplit(arr, 3)
print(newarr)
print("=====================================")
# Split by Depth
arr = np.array([[[1,  2,  3],[4,  5,  6]],[[7,  8,  9],[10, 11, 12]]])
newarr = np.dsplit(arr, 3)
print(newarr)
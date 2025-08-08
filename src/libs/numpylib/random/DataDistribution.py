from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
# If the sum of value is more than 1 it throws an error
print("=====================================")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x) # Generates 3*5 matrix
print("=====================================")

# Permutations
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
print("=====================================")
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
print("=====================================")


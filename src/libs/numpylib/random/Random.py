from numpy import random

x = random.randint(100)
print(x)
print("=====================================")
x = random.rand() # Generates float
print(x)
print("=====================================")
x=random.randint(100, size=(5))
print(x) # Generates array
print("=====================================")
x = random.randint(100, size=(3, 5))
print(x) # Generates 2D array
print("=====================================")
x = random.rand(5)
print(x) # Generates float array
print("=====================================")
x = random.rand(3, 5)
print(x) # Generates 2D array of float
print("=====================================")
x = random.choice([3, 5, 7, 9])
print(x) # Returns from array
print("=====================================")
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x) # Returns 2D array
print("=====================================")

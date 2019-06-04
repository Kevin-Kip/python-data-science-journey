import numpy as np

x1 = np.random.random((3,3)) # 3 x 5 array filled with random values
x2 = np.full((3,5), 3.2) # 3 x 5 array filled with 3.2
x3 = np.zeros((2,4), dtype=int)

print("x1 = {0}".format(x1))
print("x2 = {0}".format(x2))
print("x3 = {0}".format(x3))

print("Sum of x1 is: {0}".format(x1.sum()))
print("Max value of x1 is at index {0}".format(np.nanargmax(x1)))

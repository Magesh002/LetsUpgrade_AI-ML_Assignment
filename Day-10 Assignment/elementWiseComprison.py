import numpy as np

x = np.array([5, 8])
y = np.array([3, 8])
print("Given Numbers")
print(x)
print(y)

print("Comparison - Greater")
print(np.greater(x, y))

print("Comparison - Greater_Equal")
print(np.greater_equal(x, y))

print("Comparison - Lesser")
print(np.less(x, y))

print("Comparison - Less_Equal")
print(np.less_equal(x, y))